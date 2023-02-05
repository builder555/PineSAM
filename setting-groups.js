const settingGroups = {
  "Soldering settings": [
    "SetTemperature",
    "BoostTemperature",
    "AutoStart",
    "TempChangeShortStep",
    "TempChangeLongStep",
    "LockingMode",
  ],
  "Advanced settings": [
    "BLEEnabled",
    "PowerLimit",
    "CalibrateCJC",
    "PowerPulsePower",
    "PowerPulseWait",
    "PowerPulseDuration",
  ],
  "Power settings": [
    "DCInCutoff",
    "MinVolCell",
    "QCMaxVoltage",
    "PDNegTimeout",
  ],
  "Sleep mode": [
    "MotionSensitivity",
    "SleepTemperature",
    "SleepTimeout",
    "ShutdownTimeout",
  ],
  "User interface": [
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
  "Other": [],
};

export default settingGroups;