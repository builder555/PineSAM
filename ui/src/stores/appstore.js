import { ref, computed } from 'vue';
import { defineStore } from 'pinia';
import { socket } from '../socket';
import settingDescriptions from '../setting-descriptions.js';
import settingToComponentMap from '../setting-components.js';
export const useAppStore = defineStore('appStore', () => {
  const appInfo = ref({});
  const settings = ref({});
  const rawLiveData = ref({});
  const rawSettings = ref({});
  const peakWatts = ref(0);
  const isSaveToFlash = ref(false);
  const isBusy = ref(false);
  const error = ref('');
  const info = ref({});
  const liveData = computed(() => {
    if (Object.keys(rawLiveData.value).length < 1) return {};
    const tempInF = tempConverter[1](rawLiveData.value.LiveTemp);
    const isTempInF = settings.value.TemperatureUnit?.value === 1;
    return {
      LiveTemp: isTempInF ? tempInF : rawLiveData.value.LiveTemp,
      Voltage: (rawLiveData.value.Voltage * 0.1).toFixed(1),
      HandleTemp: (rawLiveData.value.HandleTemp * 0.1).toFixed(1),
      OperatingMode: rawLiveData.value.OperatingMode,
      Watts: (rawLiveData.value.Watts * 0.1).toFixed(1),
      PeakWatts: peakWatts.value.toFixed(1),
    };
  });
  const settingsComponents = computed(() => {
    const components = { ...settingToComponentMap };
    if (info.value?.build === '2.21') {
      components.Brightness = {
          name: 'range',
          min: 1,
          max: 101,
          step: 25,
          display: (value) => ((value - 1) / 25 + 1),
      };
    }
    return components;
  });
  
  const init = async () => {
    await fetchAppInfo();
    await fetchSettings();
    await fetchInfo();
  };

  const fetchSettings = async () => {
    isBusy.value = true;
    await socket.send({ command: 'GET_SETTINGS' });
  };

  const fetchInfo = async () => {
    isBusy.value = true;
    await socket.send({ command: 'GET_INFO' });
  };

  const fetchAppInfo = async () => {
    isBusy.value = true;
    await socket.send({ command: 'GET_APP_INFO' });
  };

  const parseSettings = () => {
    for (const name in rawSettings.value) {
      const value = Number(rawSettings.value[name]);
      settings.value[name] = {
        value,
        lastSent: value,
        display: settingDescriptions[name]?.displayText ?? name,
        hint: settingDescriptions[name]?.description ?? '',
        component: settingsComponents.value[name],
        isUpdating: false,
      };
      const isBooleanField = settingsComponents.value[name]?.name === 'checkbox';
      if (isBooleanField) {
        settings.value[name].value = value === 1;
      }
    }
    setTemperatureRanges();
    toggleVoltageSettings(settings.value.DCInCutoff.value);
  };
  const toggleHallSensorSettings = (isEnabled) => {
    const classDisabled = isEnabled ? '' : 'is-disabled';
    if (settings?.value?.HallEffectSensitivity?.component && settings.value.HallEffectSensitivity.component.class != classDisabled){
      settings.value.HallEffectSensitivity.component.class = classDisabled;
    }
  }

  const setTemperature = async (temperature) => {
    settings.value.SetTemperature.value = Number(temperature);
    updateSetting('SetTemperature', settings.value.SetTemperature.value);
  };

  const updateSetting = async (name, value) => {
    if (settings.value[name].isUpdating) return;
    value = Number(value);
    settings.value[name].isUpdating = true;
    settings.value[name].value = value;
    if (isValueOutOfLimits(name, value)) {
      const { min, max } = settings.value[name].component;
      error.value = `Value for ${name} is out of range (${min} - ${max})`;
      settings.value[name].value = settings.value[name].lastSent;
      settings.value[name].isUpdating = false;
      return;
    }
    if (settings.value[name].lastSent === value) {
      settings.value[name].isUpdating = false;
      return;
    }
    await socket.send({
      command: 'UPDATE_SETTING',
      payload: { name, value, save: isSaveToFlash.value },
    });
    settings.value[name].lastSent = value;
    const changedTempUnit = name === 'TemperatureUnit';
    const changedDCtype = name === 'DCInCutoff';
    if (changedTempUnit) setTemperatureRanges(true);
    if (changedDCtype) toggleVoltageSettings(value);
    settings.value[name].isUpdating = false;
  };

  const isValueOutOfLimits = (name, value) => {
    const { min, max, offable = false } = settings.value[name].component;
    const isMinSet = typeof min !== 'undefined';
    const isMaxSet = typeof max !== 'undefined';
    const isBelowMin = isMinSet && value < min;
    const isAboveMax = isMaxSet && value > max;
    return isAboveMax || (isBelowMin && !(offable && value == 0));
  };

  const tempConverter = {
    0: (value) => Math.round(((value - 32) * 5) / 9),
    1: (value) => Math.round((value * 9) / 5 + 32),
  };
  const setTemperatureRanges = (convertValue = false) => {
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
    const unit = settings.value.TemperatureUnit.value;
    for (const setting in ranges[unit]) {
      const [tMin, tMax] = ranges[unit][setting];
      settings.value[setting].component.min = tMin;
      settings.value[setting].component.max = tMax;
      const isOffableOff = settings.value[setting].component.offable && settings.value[setting].value === 0;
      if (convertValue && !isOffableOff) {
        settings.value[setting].value = Math.max(tMin, Math.min(tMax, tempConverter[unit](settings.value[setting].value)));
      }
    }
  };

  const toggleVoltageSettings = (value) => {
    const classHidden = value ? '' : 'is-hidden';
    settings.value.MinVolCell.component.class = classHidden;
  };

  socket.on('GET_SETTINGS', (data) => {
    rawSettings.value = data;
    parseSettings();
    isBusy.value = false;
  });
  socket.on('GET_INFO', (data) => {
    info.value = data;
    parseSettings();
    isBusy.value = false;
  });
  socket.on('GET_APP_INFO', (data) => {
    appInfo.value = data;
    isBusy.value = false;
  });
  socket.on('LIVE_DATA', (data) => {
    if (error.value == 'Device not found' || error.value == 'Device disconnected') {
      error.value = '';
      init();
    }
    rawLiveData.value = data;
    const watts = liveData.value.Watts;
    if (watts > peakWatts.value) {
      peakWatts.value = Math.max(watts, peakWatts.value);
    }
    toggleHallSensorSettings(!!rawLiveData.value?.HallSensor);
  });
  socket.on('ERROR', (data) => {
    error.value = data;
    isBusy.value = false;
  });

  return {
    appInfo,
    error,
    fetchSettings,
    info,
    init,
    isBusy,
    isSaveToFlash,
    liveData,
    rawLiveData,
    setTemperature,
    settings,
    updateSetting,
  };
});
