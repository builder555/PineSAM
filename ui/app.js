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
      for (const name in rawSettings) {
        const value = Number(rawSettings[name]);
        this.settings[name] = {
          value,
          display: settingDescriptions[name]?.displayText ?? name,
          hint: settingDescriptions[name]?.description ?? '',
          component: settingToComponentMap[name],
        }
        if (settingToComponentMap[name]?.name === 'checkbox') {
          this.settings[name].value = value === 1;
        }
        this.$watch(`settings.${name}.value`, debounce((newValue, oldValue) => {
          if (newValue !== oldValue) {
            this.updateSetting(name, newValue);
          }
        }, 500));
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
      this.isBusy = true;
      value = Number(value);
      this.checkSocket()
      .then(() => {
        this.socket.send(JSON.stringify({command: "UPDATE_SETTING", payload: {name, value, save: this.saveToFlash}}));
      });
      if (name === 'TemperatureUnit') {
        this.setTemperatureRanges(true);
      }
      if (name === 'DCInCutoff') {
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
        this.isBusy = false;
        const data = JSON.parse(event.data)
        if (data.status == 'ERROR') {
          console.warn('error!', data);
          this.error = data.message;
        }
        if (data.command === "GET_SETTINGS") {
          this.parseSettings(data.payload);
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
