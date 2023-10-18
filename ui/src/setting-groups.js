const settingGroups = [
  {
    name: 'Soldering settings',
    isVisible: true,
    items: [
      'SetTemperature',
      'BoostTemperature',
      'AutoStart',
      'TempChangeShortStep',
      'TempChangeLongStep',
      'LockingMode',
    ],
  },
  {
    name: 'Sleep mode',
    isVisible: true,
      items: ['MotionSensitivity', 'SleepTemperature', 'SleepTimeout', 'ShutdownTimeout', 'HallEffectSensitivity'],
  },
  {
    name: 'Power settings',
    isVisible: true,
    items: ['DCInCutoff', 'MinVolCell', 'QCMaxVoltage', 'PDNegTimeout'],
  },
  {
    name: 'User interface',
    isVisible: true,
    items: [
      'TemperatureUnit',
      'DisplayRotation',
      'CooldownBlink',
      'ScrollingSpeed',
      'ReverseButtonTempChange',
      'AnimSpeed',
      'Brightness',
      'ColourInversion',
      'LOGOTime',
      'AdvancedIdle',
      'AdvancedSoldering',
    ],
  },
  {
    name: 'Advanced settings',
    isVisible: true,
    items: ['PowerLimit', 'CalibrateCJC', 'PowerPulsePower', 'PowerPulseWait', 'PowerPulseDuration', 'SettingsReset'],
  },
  {
    name: 'Unused',
    isVisible: false,
    items: [
      // "Write 1 to save",
      'AccelMissingWarningCounter',
      'AnimLoop',
      'CalibrationOffset',
      'PDMissingWarningCounter',
      'UILanguage',
      // "VoltageCalibration",
    ],
  },
];

export default settingGroups;
