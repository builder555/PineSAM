// copied from https://github.com/Ralim/IronOS/blob/dev/Translations/translation_EN.json
const settingDescriptions = {
  DCInCutoff: {
    displayText: 'Power source',
    description: 'Set cutoff voltage to prevent battery overdrainage (DC 10V) (S=3.3V per cell, disable PWR limit)',
  },
  MinVolCell: {
    displayText: 'Minimum voltage',
    description: 'Minimum allowed voltage per battery cell (3S: 3 - 3.7V | 4-6S: 2.4 - 3.7V)',
  },
  QCMaxVoltage: {
    displayText: 'QC voltage',
    description: 'Max QC voltage the iron should negotiate for',
  },
  PDNegTimeout: {
    displayText: 'PD timeout',
    description: 'PD negotiation timeout in 100ms steps for compatibility with some QC chargers',
  },
  SetTemperature: {
    displayText: 'Soldering temp',
    description: 'Tip temperature used in normal soldering mode',
  },
  BoostTemperature: {
    displayText: 'Boost temp',
    description: 'Tip temperature used in "boost mode"',
  },
  AutoStart: {
    displayText: 'Start-up behavior',
    description:
      'O=off | S=heat to soldering temp | Z=standby at sleep temp until moved | R=standby without heating until moved',
  },
  TempChangeShortStep: {
    displayText: 'Temp change short',
    description: 'Temperature-change-increment on short button press',
  },
  TempChangeLongStep: {
    displayText: 'Temp change long',
    description: 'Temperature-change-increment on long button press',
  },
  LockingMode: {
    displayText: 'Allow locking buttons',
    description:
      'While soldering, hold down both buttons to toggle locking them (D=disable | B=boost mode only | F=full locking)',
  },
  MotionSensitivity: {
    displayText: 'Motion sensitivity',
    description: '0=off | 1=least sensitive | ... | 9=most sensitive',
  },
  SleepTemperature: {
    displayText: 'Sleep temp',
    description: 'Tip temperature while in "sleep mode"',
  },
  SleepTimeout: {
    displayText: 'Sleep timeout',
    description: 'Interval before "sleep mode" starts (s=seconds | m=minutes)',
  },
  ShutdownTimeout: {
    displayText: 'Shutdown timeout',
    description: 'Interval before the iron shuts down (m=minutes)',
  },
  HallEffectSensitivity: {
    displayText: 'Hall sensor sensitivity',
    description: 'Sensitivity to magnets (0=off | 1=least sensitive | ... | 9=most sensitive). Only available if there is a Hall Effect Sensor installed.',
  },
  TemperatureUnit: {
    displayText: 'Temperature unit',
    description: 'C=°Celsius | F=°Fahrenheit',
  },
  DisplayRotation: {
    displayText: 'Display orientation',
    description: 'R=right-handed | L=left-handed | A=automatic',
  },
  CooldownBlink: {
    displayText: 'Cooldown flashing',
    description: 'Flash temp reading at idle while tip is hot',
  },
  ScrollingSpeed: {
    displayText: 'Scrolling speed',
    description: 'Scrolling speed of info text (S=slow | F=fast)',
  },
  ReverseButtonTempChange: {
    displayText: 'Swap + - keys',
    description: 'Reverse assignment of buttons for temperature adjustment',
  },
  AnimSpeed: {
    displayText: 'Anim. speed',
    description: 'Pace of icon animations in menu (O=off | S=slow | M=medium | F=fast)',
  },
  AnimLoop: {
    displayText: 'Anim. loop',
    description: 'Loop icon animations in main menu',
  },
  Brightness: {
    displayText: 'Screen brightness',
    description: 'Adjust the OLED screen brightness',
  },
  ColourInversion: {
    displayText: 'Invert screen',
    description: 'Invert the OLED screen colors',
  },
  LOGOTime: {
    displayText: 'Boot logo duration',
    description: 'Set boot logo duration (s=seconds)',
  },
  AdvancedIdle: {
    displayText: 'Detailed idle screen',
    description: 'Display detailed info in a smaller font on idle screen',
  },
  AdvancedSoldering: {
    displayText: 'Detailed solder screen',
    description: 'Display detailed info in a smaller font on soldering screen',
  },
  PowerLimit: {
    displayText: 'Power limit',
    description: 'Maximum power the iron can use (W=watt)',
  },
  CalibrateCJC: {
    displayText: 'Calibrate CJC at next boot',
    description: 'Calbrate Cold Junction Compensation at next boot (not required if Delta T is < 5°C)',
  },
  VoltageCalibration: {
    displayText: 'Calibrate input voltage',
    description: 'Start VIN calibration (long press to exit)',
  },
  PowerPulsePower: {
    displayText: 'Power pulse',
    description: 'Intensity of power of keep-awake-pulse (W=watt)',
  },
  PowerPulseWait: {
    displayText: 'Power pulse delay',
    description: 'Delay before keep-awake-pulse is triggered (x 2.5s)',
  },
  PowerPulseDuration: {
    displayText: 'Power pulse duration',
    description: 'Keep-awake-pulse duration (x 250ms)',
  },
  SettingsReset: {
    displayText: 'Restore default settings',
    description: 'Reset all settings to default',
  },
  LanguageSwitch: {
    displayText: 'Language:  EN     English',
    description: '',
  },
  BLEEnabled: {
    displayText: 'BLE  Enabled',
    description: 'Enables BLE. If you disable it, you will not be able to use this app',
  },
};

export default settingDescriptions;
