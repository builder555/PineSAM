# values copied from https://github.com/Ralim/IronOS/blob/662829ebd9530e83c460f7c5dfcd2d0ea8ff401e/source/Core/Src/Settings.cpp
MAX_TEMP_C = 450
MAX_TEMP_F = 850
MIN_TEMP_C =  10
MIN_TEMP_F =  50
MIN_BOOST_TEMP_C = 250
MIN_BOOST_TEMP_F = 480
MAX_SLEEP_TEMP_C = 300
MAX_SLEEP_TEMP_F = 570

value_limits = {
    "SetTemperature":               [MIN_TEMP_C, MAX_TEMP_F],
    "SleepTemperature":             [MIN_TEMP_C, MAX_TEMP_F],
    "SleepTimeout":                 [0, 15],
    "DCInCutoff":                   [0, 4],
    "MinVolCell":                   [24, 38],
    "QCMaxVoltage":                 [90, 220],
    "DisplayRotation":              [0, 2],
    "MotionSensitivity":            [0, 9],
    "AnimLoop":                     [0, 1],
    "AnimSpeed":                    [0, 3],
    "AutoStart":                    [0, 3],
    "ShutdownTimeout":              [0, 60],
    "CooldownBlink":                [0, 1],
    "AdvancedIdle":                 [0, 1],
    "AdvancedSoldering":            [0, 1],
    "TemperatureUnit":              [0, 1],
    "ScrollingSpeed":               [0, 1],
    "LockingMode":                  [0, 2],
    "PowerPulsePower":              [0, 99],
    "PowerPulseWait":               [1, 9],
    "PowerPulseDuration":           [1, 9],
    "VoltageCalibration":           [360, 900],
    "BoostTemperature":             [0, MAX_TEMP_F],
    "CalibrationOffset":            [100, 2500],
    "PowerLimit":                   [0, 220],
    "ReverseButtonTempChange":      [0, 1],
    "TempChangeLongStep":           [5, 90],
    "TempChangeShortStep":          [1, 50],
    "HallEffectSensitivity":        [0, 9],
    "AccelMissingWarningCounter":   [0, 9],
    "PDMissingWarningCounter":      [0, 9],
    "UILanguage":                   [0, 0xFFFF],
    "PDNegTimeout":                 [0, 50],
    "ColourInversion":              [0, 1],
    "Brightness":                   [0, 101],
    "LOGOTime":                     [0, 5],
    "CalibrateCJC":                 [0, 1],
    "BLEEnabled":                   [0, 1],
    "SettingsReset":                [0, 0xFFFF],
    "save_to_flash":                 [0, 1],
}

temperature_limits = {
    'SetTemperature': { 
        0: lambda t: MIN_TEMP_C<=t<=MAX_TEMP_C,
        1 :lambda t: MIN_TEMP_F<=t<=MAX_TEMP_F
    },
    'SleepTemperature': {
        0: lambda t: MIN_TEMP_C<=t<=MAX_SLEEP_TEMP_C,
        1: lambda t: MIN_TEMP_F<=t<=MAX_SLEEP_TEMP_F,
    },
    'BoostTemperature': {
        0: lambda t: MIN_BOOST_TEMP_C<=t<=MAX_TEMP_C or t==0,
        1: lambda t: MIN_BOOST_TEMP_F<=t<=MAX_TEMP_F or t==0,
    },
}
