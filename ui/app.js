import settingGroups from "./setting-groups.js";
import settingDescriptions from "./setting-descriptions.js";
import settingToComponentMap from "./setting-components.js";
import { wakeLock } from "./pwa.js";

const getLocalStorageValue = (key, defaultValue) => {
  const value = localStorage.getItem(key);
  if (value === null) {
    return defaultValue;
  }
  return JSON.parse(value);
};

export default {
  data: () => ({
    settings: {},
    groups: settingGroups,
    saveToFlash: false,
    isBusy: false,
    info: {},
    socket: null,
    error: "",
    isNameHidden: true,
    isHintVisible: false,
    liveDataRaw: {},
    holdingBtnTimer: false,
    isPlusMinusHeld: false,
    preventClick: false,
    presets: [],
    peakWatts: 0.0,
  }),
  computed: {
    liveData() {
      if (Object.keys(this.liveDataRaw).length < 1) return {};
      return {
        LiveTemp: this.liveDataRaw.LiveTemp,
        Voltage: (this.liveDataRaw.Voltage * 0.1).toFixed(1),
        HandleTemp: (this.liveDataRaw.HandleTemp * 0.1).toFixed(1),
        OperatingMode: this.liveDataRaw.OperatingMode,
        Watts: (this.liveDataRaw.Watts * 0.1).toFixed(1),
        PeakWatts: (this.peakWatts).toFixed(1),
      };
    },
  },
  methods: {
    getLocalGroupVisibilities() {
      for (const group of this.groups) {
        group.isVisible = getLocalStorageValue(
          `setting-${group.name}-visible`,
          true,
        );
      }
    },
    getLocalTemperaturePresets() {
      this.presets = getLocalStorageValue(`presets`, ["315", "365"]);
    },
    parseSettings(rawSettings) {
      for (const name in rawSettings) {
        const value = Number(rawSettings[name]);
        this.settings[name] = {
          value,
          lastSent: value,
          display: settingDescriptions[name]?.displayText ?? name,
          hint: settingDescriptions[name]?.description ?? "",
          component: settingToComponentMap[name],
          showRawValue: false,
          isUpdating: false,
        };
        const isBooleanField = settingToComponentMap[name]?.name === "checkbox";
        if (isBooleanField) {
          this.settings[name].value = value === 1;
        }
        const isRapidlyChangingField =
          settingToComponentMap[name]?.name === "range";
        if (!isRapidlyChangingField) {
          this.$watch(`settings.${name}.value`, (value) => {
            this.updateSetting(name, value);
          });
        }
        this.$watch(`settings.${name}.showRawValue`, (isShow) => {
          if (isShow) {
            this.$nextTick(() => {
              this.$refs[name][0].focus();
            });
          }
        });
        if (name === "SettingsReset") {
          const advanced = this.groups.find((group) =>
            group.name === "Advanced settings"
          );
          if (advanced.items.indexOf("SettingsReset") < 0) {
            advanced.items.push("SettingsReset");
          }
        }
      }
      this.setTemperatureRanges();
      this.toggleVoltageSettings(this.settings["DCInCutoff"].value);
    },
    confirm(name, message = "Are you sure?", callback = false) {
      const yes = window.confirm(message);
      if (yes && name === "SettingsReset") {
        this.updateSetting(name, 1);
      } else if (yes && name == "SetPreset") {
        if (callback) {
          callback();
        }
      }
    },
    toggleGroup(group) {
      group.isVisible = !group.isVisible;
      localStorage.setItem(`setting-${group.name}-visible`, group.isVisible);
    },
    onPresetBtnDown(idx) {
      const setTemp = this.settings.SetTemperature.value;
      this.holdingBtnTimer = setTimeout(() => {
        this.confirm(
          "SetPreset",
          `Are you sure you wish to set this preset to ${setTemp}?`,
          () => this.presets[idx] = setTemp,
        );
        localStorage.setItem("presets", JSON.stringify(this.presets));
        this.holdingBtnTimer = null;
      }, 1000);
    },
    onPresetBtnUp() {
      if (this.holdingBtnTimer) clearTimeout(this.holdingBtnTimer);
      this.holdingBtnTimer = null;
    },
    setExactTemperature(temperature) {
      this.settings.SetTemperature.value = Number(temperature);
      this.updateSetting("SetTemperature", this.settings.SetTemperature.value);
    },
    changeTemperature(direction) {
      if (this.isPlusMinusHeld) return;
      const currentSetTemp = this.settings.SetTemperature.value;
      const step = this.settings.TempChangeShortStep.value;
      this.setExactTemperature(currentSetTemp + direction * step);
    },
    onChangeTempBtnDown(direction) {
      const step = this.settings.TempChangeLongStep.value;
      const updateTemperature = () => {
        this.isPlusMinusHeld = true;
        this.setExactTemperature(this.settings.SetTemperature.value + direction * step);
      };
      this.holdingBtnTimer = setInterval(() => {
        updateTemperature();
        clearInterval(this.holdingBtnTimer);
        // speed up the temperature change
        this.holdingBtnTimer = setInterval(updateTemperature, 600);
      }, 1000);
    },
    onChangeTempBtnUp() {
      if (this.holdingBtnTimer) {
        setTimeout(() => { // to ensure "onClick" doesn't update the temperature
          clearInterval(this.holdingBtnTimer);
          this.holdingBtnTimer = null;
          this.isPlusMinusHeld = false;
        },0);
      }
    },
    setTemperatureRanges(convertValue = false) {
      const ranges = {
        0: {
          BoostTemperature: [250, 450],
          SetTemperature: [10, 450],
          SleepTemperature: [10, 300],
        },
        1: {
          BoostTemperature: [480, 840],
          SetTemperature: [60, 850],
          SleepTemperature: [60, 580],
        },
      };
      const converter = {
        0: (value) => Math.round((value - 32) * 5 / 9),
        1: (value) => Math.round(value * 9 / 5 + 32),
      };
      const unit = this.settings["TemperatureUnit"].value;
      for (const setting in ranges[unit]) {
        const [tMin, tMax] = ranges[unit][setting];
        this.settings[setting].component.min = tMin;
        this.settings[setting].component.max = tMax;
        const isBoostTempOff = setting === "BoostTemperature" &&
          this.settings["BoostTemperature"].value === 0;
        if (convertValue && !(isBoostTempOff)) {
          this.settings[setting].value = Math.max(
            tMin,
            Math.min(tMax, converter[unit](this.settings[setting].value)),
          );
        }
      }
    },
    toggleVoltageSettings(value) {
      const classHidden = value ? "" : "is-hidden";
      this.settings["MinVolCell"].component.class = classHidden;
    },
    isValueOutOfLimits(name, value) {
      const { min, max, offable = false } = this.settings[name].component;
      const isMinSet = typeof min !== "undefined";
      const isMaxSet = typeof max !== "undefined";
      const isBelowMin = isMinSet && value < min;
      const isAboveMax = isMaxSet && value > max;
      return isAboveMax || isBelowMin && !(offable && value == 0);
    },
    updateSetting(name, value) {
      if (this.settings[name].isUpdating) return;
      this.settings[name].isUpdating = true;
      if (this.isValueOutOfLimits(name, value)) {
        const { min, max } = this.settings[name].component;
        this.error = `Value for ${name} is out of range (${min} - ${max})`;
        this.settings[name].value = this.settings[name].lastSent;
        this.settings[name].isUpdating = false;
        return;
      }
      if (this.settings[name].showRawValue) {
        this.settings[name].showRawValue = false;
      }
      value = Number(value);
      if (this.settings[name].lastSent === value) {
        this.settings[name].isUpdating = false;
        return;
      }
      this.checkSocket()
        .then(() => {
          this.socket.send(
            JSON.stringify({
              command: "UPDATE_SETTING",
              payload: { name, value, save: this.saveToFlash },
            }),
          );
          this.settings[name].lastSent = value;
        })
        .finally(() => this.settings[name].isUpdating = false);
      const changedTempUnit = name === "TemperatureUnit";
      const changedDCtype = name === "DCInCutoff";
      if (changedTempUnit) this.setTemperatureRanges(true);
      if (changedDCtype) this.toggleVoltageSettings(value);
      this.settings[name].isUpdating = false;
    },
    checkSocket() {
      this.isBusy = true;
      return new Promise((resolve, reject) => {
        if (this.socket.readyState !== WebSocket.OPEN) {
          this.initSocket(false);
          this.socket.onopen = () => {
            resolve();
          };
        } else {
          resolve();
        }
      });
    },
    fetchSettings() {
      this.checkSocket()
        .then(() => {
          this.socket.send(JSON.stringify({ command: "GET_SETTINGS" }));
        });
    },
    fetchInfo() {
      this.checkSocket()
        .then(() => {
          this.socket.send(JSON.stringify({ command: "GET_INFO" }));
        });
    },
    initSocket(fetchData = true) {
      this.isBusy = true;
      this.socket = new WebSocket(`ws://${window.location.hostname}:12999/`);
      this.socket.onopen = () => {
        this.isBusy = false;
        if (fetchData) {
          this.fetchSettings();
          this.fetchInfo();
        }
      };
      this.socket.onmessage = (event) => {
        this.isBusy = false;
        const data = JSON.parse(event.data);
        if (data.status == "ERROR") {
          console.warn("error!", data);
          this.error = data.message;
          return;
        }
        if (data.command === "GET_SETTINGS") {
          this.parseSettings(data.payload);
        }
        if (data.command === "GET_INFO") {
          this.info = data.payload;
        }
        if (data.command === "LIVE_DATA") {
          this.liveDataRaw = data.payload;
          const watts = this.liveData["Watts"];
          if (watts > this.peakWatts) {
            this.peakWatts = Math.max(watts, this.peakWatts);
          }
        }
      };
      this.socket.onclose = () => {
        this.isBusy = false;
        console.log("socket closed");
      };
      this.socket.onerror = (e) => {
        this.isBusy = false;
        this.error =
          "Error connecting to backend. Make sure the server is running.";
        console.warn("error!", e);
      };
    },
  },
  mounted() {
    this.getLocalGroupVisibilities();
    this.getLocalTemperaturePresets();
    this.initSocket();
    wakeLock.request().then((lock) => {
      this.awake = lock;
    });
  },
  beforeUnmount() {
    wakeLock.release(this.awake);
  },
};
