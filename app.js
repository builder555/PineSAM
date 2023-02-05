let socket = new WebSocket("ws://localhost:12999");

import settingNames from "./setting-names.js";
import settingGroups from "./setting-groups.js";
import settingDescriptions from "./setting-descriptions.js";

const settingToComponentMap = {
  BLEEnabled: { name: 'checkbox' },
  AdvancedIdle: { name: 'checkbox' },
  AdvancedSoldering: { name: 'checkbox' },
  CooldownBlink: { name: 'checkbox' },
  ReverseButtonTempChange: { name: 'checkbox' },
  ColourInversion: { name: 'checkbox' },
  CalibrateCJC: { name: 'checkbox' },
  DCInCutoff: {
    name: 'select',
    options: [
      { value: 0, text: "DC" },
      { value: 1, text: "3S" },
      { value: 2, text: "4S" },
      { value: 3, text: "5S" },
      { value: 4, text: "6S" },
    ],
  },
  AutoStart: {
    name: 'select',
    options: [
      { value: 0, text: "O" },
      { value: 1, text: "S" },
      { value: 2, text: "Z" },
      { value: 3, text: "R" },
    ],
  },
  LockingMode: {
    name: 'select',
    options: [
      { value: 0, text: "D" },
      { value: 1, text: "B" },
      { value: 2, text: "F" },
    ],
  },
  TemperatureUnit: {
    name: 'select',
    options: [
      { value: 0, text: "C" },
      { value: 1, text: "F" },
    ],
  },
  SleepTimeout: {
    name: 'select',
    options: [
      { value: 0, text: "Off" },
      { value: 1, text: "10s" },
      { value: 2, text: "20s" },
      { value: 3, text: "30s" },
      { value: 4, text: "40s" },
      { value: 5, text: "50s" },
      { value: 6, text: "1m" },
      { value: 7, text: "2m" },
      { value: 8, text: "3m" },
      { value: 9, text: "4m" },
      { value: 10, text: "5m" },
      { value: 11, text: "6m" },
      { value: 12, text: "7m" },
      { value: 13, text: "8m" },
      { value: 14, text: "9m" },
      { value: 15, text: "10m" },
    ],
  },
  DisplayRotation: {
    name: 'select',
    options: [
      { value: 0, text: "R" },
      { value: 1, text: "L" },
      { value: 2, text: "A" },
    ],
  },
  ScrollingSpeed: {
    name: 'select',
    options: [
      { value: 0, text: "S" },
      { value: 1, text: "F" },
    ],
  },
  AnimSpeed: {
    name: 'select',
    options: [
      { value: 0, text: "O" },
      { value: 1, text: "S" },
      { value: 2, text: "M" },
      { value: 3, text: "F" },
    ],
  },
  LOGOTime: {
    name: 'select',
    options: [
      { value: 0, text: "Off" },
      { value: 1, text: "1s" },
      { value: 2, text: "2s" },
      { value: 3, text: "3s" },
      { value: 4, text: "4s" },
      { value: 5, text: "∞" },
    ],
  },
  QCMaxVoltage: {
    name: 'range',
    min: 90,
    max: 220,
    step: 2,
    display: (value) => value / 10,
  },
  MinVolCell: {
    name: 'range',
    min: 24,
    max: 38,
    step: 1,
    display: (value) => value / 10,
  },
  PDNegTimeout: {
    name: 'range',
    min: 0,
    max: 50,
    step: 1,
  },
  MotionSensitivity: {
    name: 'range',
    min: 0,
    max: 9,
    step: 1,
  },
  SleepTemperature: {
    name: 'range',
    min: 10,
    max: 300,
    step: 10,
  },
  ShutdownTimeout: {
    name: 'range',
    min: 0,
    max: 60,
    step: 1,
    display: (value) => value == 0 ? "Off" : `${value}m`,
  },
  SetTemperature: {
    name: 'range',
    min: 10,
    max: 450,
    step: 1,
  },
  TempChangeShortStep: {
    name: 'range',
    min: 1,
    max: 50,
    step: 1,
  },
  TempChangeLongStep: {
    name: 'range',
    min: 5,
    max: 90,
    step: 5,
  },
  PowerLimit: {
    name: 'range',
    min: 0,
    max: 220,
    step: 5,
    display: (value) => value == 0 ? "Off" : `${value}W`,
  },
  PowerPulsePower: {
    name: 'range',
    min: 0,
    max: 99,
    step: 1,
    display: (value) => value == 0 ? "Off" : `${value/10}W`,
  },
  PowerPulseWait: {
    name: 'range',
    min: 1,
    max: 9,
    step: 1,
  },
  PowerPulseDuration: {
    name: 'range',
    min: 1,
    max: 9,
    step: 1,
  },
  Brightness: {
    name: 'range',
    min: 0,
    max: 99,
    step: 11,
    display: (value) => value == 0 ? "Off" : value/11 + 1,
  },
  BoostTemperature: {
    name: 'range',
    min: 260,
    max: 450,
    step: 10,
    offable: true,
    display: (value) => value == 0 ? "Off" : value,
  },
};

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
    isBusy: true,
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
    },
    toggleGroup(group) {
      group.isVisible = !group.isVisible;
      localStorage.setItem(`setting-${group.name}-visible`, group.isVisible);
    },
    updateSetting(uuid, value) {
      socket = new WebSocket("ws://localhost:12999");
      value = Number(value);
      socket.onopen = () => {
        socket.send(JSON.stringify({command: "UPDATE_SETTING", payload: {uuid: uuid, value, save: this.saveToFlash}}));
      };
    },
  },
  mounted() {
    this.getLocalGroupVisibilities();
    socket.onopen = () => {
      this.isBusy = true;
      socket.send(JSON.stringify({command: "GET_SETTINGS"}));
    };
    socket.onmessage = (event) => {
      this.parseSettings(JSON.parse(event.data));
      this.isBusy = false;
    };
    socket.onclose = () => {
      this.isBusy = false;
    };
    socket.onerror = () => {
      this.isBusy = false;
    };
  },
};
