import settingGroups from "./setting-groups.js";
import settingDescriptions from "./setting-descriptions.js";
import settingToComponentMap from "./setting-components.js";

const getLocalStorageValue = (key, defaultValue) => {
  const value = localStorage.getItem(key);
  if (value === null) {
    return defaultValue;
  }
  return JSON.parse(value);
};

const debounce = (fn, wait) => {
  let timeout;
  return (...args) => {
    clearTimeout(timeout);
    timeout = setTimeout(() => fn(...args), wait);
  };
};

export default {
  data: () => ({
    settings: { },
    groups: settingGroups,
    saveToFlash: false,
    isBusy: false,
    info : {},
    socket: null,
    error: '',
  }),
  methods: {
    getLocalGroupVisibilities() {
      for(const group of this.groups) {
        group.isVisible = getLocalStorageValue(`setting-${group.name}-visible`, true);
      }
    },
    parseSettings(rawSettings) {
      for (const name in rawSettings) {
        const value = Number(rawSettings[name]);
        this.settings[name] = {
          value,
          lastSent: value,
          display: settingDescriptions[name]?.displayText ?? name,
          hint: settingDescriptions[name]?.description ?? '',
          component: settingToComponentMap[name],
          showRawValue: false,
        }
        const isBooleanField = settingToComponentMap[name]?.name === 'checkbox';
        if (isBooleanField) {
          this.settings[name].value = value === 1;
        }
        const isRapidlyChangingField = settingToComponentMap[name]?.name === 'range';
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
        if (name === 'SettingsReset') {
          const advanced = this.groups.find(group => group.name === 'Advanced settings');
          if (advanced.items.indexOf('SettingsReset')<0) advanced.items.push('SettingsReset');
        }
      }
      this.setTemperatureRanges();
      this.toggleVoltageSettings(this.settings['DCInCutoff'].value);
    },
    confirm(name){
      const yes = window.confirm('Are you sure?');
      if (yes && name === 'SettingsReset') {
          this.updateSetting(name, 1);
      }
    },
    toggleGroup(group) {
      group.isVisible = !group.isVisible;
      localStorage.setItem(`setting-${group.name}-visible`, group.isVisible);
    },
    setTemperatureRanges(convertValue=false) {
      const ranges = {
        0 : {
          BoostTemperature: [250, 450],
          SetTemperature: [10, 450],
          SleepTemperature: [10, 300],
        },
        1 : {
          BoostTemperature: [480, 840],
          SetTemperature: [60, 850],
          SleepTemperature: [60, 580],
        },
      };
      const converter = {
        0: (value) => Math.round((value - 32) * 5 / 9),
        1: (value) => Math.round(value * 9 / 5 + 32),
      }
      const unit = this.settings['TemperatureUnit'].value;
      for (const setting in ranges[unit]) {
        const [tMin,tMax] = ranges[unit][setting];
        this.settings[setting].component.min = tMin;
        this.settings[setting].component.max = tMax;
        const isBoostTempOff = setting === 'BoostTemperature' && this.settings['BoostTemperature'].value === 0;
        if (convertValue && !(isBoostTempOff)) {
          this.settings[setting].value = Math.max(tMin, Math.min(tMax,converter[unit](this.settings[setting].value)));
        }
      }
    },
    toggleVoltageSettings(value) {
      const classHidden = value ? '' : 'is-hidden';
      this.settings['MinVolCell'].component.class = classHidden;
    },
    updateSetting(name, value) {
      // check if value is within valid range:
      const {min, max, offable} = this.settings[name].component;
      if ((value < min && (value > 0 || !offable)) || value > max) {
        this.error = `Value for ${name} is out of range (${min} - ${max})`;
        this.settings[name].value = this.settings[name].lastSent;
        return;
      }
      if (this.settings[name].showRawValue) this.settings[name].showRawValue=false;
      value = Number(value);
      if (this.settings[name].lastSent === value) return;
      this.checkSocket()
      .then(() => {
        this.socket.send(JSON.stringify({command: "UPDATE_SETTING", payload: {name, value, save: this.saveToFlash}}));
        this.settings[name].lastSent = value;
      });
      const changedTempUnit = name === 'TemperatureUnit';
      const changedDCtype = name === 'DCInCutoff';
      if (changedTempUnit) this.setTemperatureRanges(true);
      if (changedDCtype) this.toggleVoltageSettings(value)
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
        this.socket.send(JSON.stringify({command: "GET_SETTINGS"}));
      });
    },
    fetchInfo() {
      this.checkSocket()
      .then(() => {
        this.socket.send(JSON.stringify({command: "GET_INFO"}));
      });
    },
    initSocket(fetchData=true) {
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
        const data = JSON.parse(event.data)
        if (data.status == 'ERROR') {
          console.warn('error!', data);
          this.error = data.message;
          return;
        }
        if (data.command === "GET_SETTINGS") {
          this.parseSettings(data.payload);
        }
        if (data.command === "GET_INFO") {
          this.info = data.payload;
        }
      };
      this.socket.onclose = () => {
        this.isBusy = false;
        console.log('socket closed');
      };
      this.socket.onerror = (e) => {
        this.isBusy = false;
        this.error = 'Error connecting to backend. Make sure the server is running.'
        console.warn('error!', e);
      };
    },
  },
  mounted() {
    this.getLocalGroupVisibilities();
    this.initSocket();
  },
};
