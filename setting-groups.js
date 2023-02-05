const settingGroups = [
  {
    name: "Soldering settings",
    isVisible: true,
    items: [
      "SetTemperature",
      "BoostTemperature",
      "AutoStart",
      "TempChangeShortStep",
      "TempChangeLongStep",
      "LockingMode",
    ],
  },
  {
    name: "Advanced settings",
    isVisible: true,
    items: [
      "PowerLimit",
      "CalibrateCJC",
      "PowerPulsePower",
      "PowerPulseWait",
      "PowerPulseDuration",
    ],
  },
  {
    name: "Power settings",
    isVisible: true,
    items: [
      "DCInCutoff",
      "MinVolCell",
      "QCMaxVoltage",
      "PDNegTimeout"
    ],
  },
  {
    name: "Sleep mode",
    isVisible: true,
    items: [
      "MotionSensitivity",
      "SleepTemperature",
      "SleepTimeout",
      "ShutdownTimeout",
    ],
  },
  {
    name: "User interface",
    isVisible: true,
    items: [
      "TemperatureUnit",
      "DisplayRotation",
      "CooldownBlink",
      "ScrollingSpeed",
      "ReverseButtonTempChange",
      "AnimSpeed",
      "Brightness",
      "ColourInversion",
      "LOGOTime",
      "AdvancedIdle",
      "AdvancedSoldering",
    ],
  },
  {
    name: "Unused",
    isVisible: false,
    items: [
      // "Write 1 to save",
      "AccelMissingWarningCounter",
      "AnimLoop",
      "CalibrationOffset",
      "HallEffectSensitivity",
      "PDMissingWarningCounter",
      "UILanguage",
      // "VoltageCalibration",
    ]
  }
];

export default settingGroups;
