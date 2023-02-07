import settingNames from "./setting-names.js";
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
      for (const uuid in rawSettings) {
        const value = Number(rawSettings[uuid]);
        const name = settingNames[uuid] ?? uuid;
        this.settings[name] = {
          value,
          uuid,
          display: settingDescriptions[name]?.displayText ?? name,
          hint: settingDescriptions[name]?.description ?? '',
          component: settingToComponentMap[name],
        }
        if (settingToComponentMap[name]?.name === 'checkbox') {
          this.settings[name].value = value === 1;
        }
        this.$watch(`settings.${name}.value`, debounce((newValue, oldValue) => {
          if (newValue !== oldValue) {
            this.updateSetting(uuid, newValue);
          }
        }, 500));
      }
      this.setTemperatureRanges();
      this.toggleVoltageSettings(this.settings['DCInCutoff'].value);
    },
    toggleGroup(group) {
      group.isVisible = !group.isVisible;
      localStorage.setItem(`setting-${group.name}-visible`, group.isVisible);
    },
    setTemperatureRanges(convertValue=false) {
      const ranges = {
        0 : {
          BoostTemperature: [260, 450],
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
        this.settings[setting].component.min = ranges[unit][setting][0];
        this.settings[setting].component.max = ranges[unit][setting][1];
        if (convertValue) {
          this.settings[setting].value = converter[unit](this.settings[setting].value);
        }
      }
    },
    toggleVoltageSettings(value) {
      const classHidden = value ? '' : 'is-hidden';
      this.settings['MinVolCell'].component.class = classHidden;
      this.settings['QCMaxVoltage'].component.class = classHidden;
      this.settings['PDNegTimeout'].component.class = classHidden;
    },
    updateSetting(uuid, value) {
      this.isBusy = true;
      value = Number(value);
      this.checkSocket()
      .then(() => {
        this.socket.send(JSON.stringify({command: "UPDATE_SETTING", payload: {uuid: uuid, value, save: this.saveToFlash}}));
      });
      if (settingNames[uuid] === 'TemperatureUnit') {
        this.setTemperatureRanges(true);
      }
      if (settingNames[uuid] === 'DCInCutoff') {
        this.toggleVoltageSettings(value)
      }
    },
    checkSocket() {
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
      if (this.isBusy) return;
      this.isBusy = true;
      this.checkSocket()
      .then(() => {
        this.socket.send(JSON.stringify({command: "GET_SETTINGS"}));
      });
    },
    initSocket(fetchSettings=true) {
      this.socket = new WebSocket(`ws://${window.location.hostname}:12999/`);
      this.socket.onopen = () => {
        if (fetchSettings) this.fetchSettings();
      };
      this.socket.onmessage = (event) => {
        const data = JSON.parse(event.data)
        if (data.status == 'ERROR') {
          console.warn('error!', data);
          this.error = data.message;
        }
        if (data.command === "GET_SETTINGS") {
          this.parseSettings(data.payload);
        }
        this.isBusy = false;
      };
      this.socket.onclose = () => {
        console.log('socket closed');
        this.isBusy = false;
      };
      this.socket.onerror = (e) => {
        this.error = 'Error connecting to backend. Make sure the server is running.'
        console.warn('error!', e);
        this.isBusy = false;
      };
    },
  },
  mounted() {
    this.getLocalGroupVisibilities();
    this.initSocket();
  },
};
