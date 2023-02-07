# values copied from https://github.com/Ralim/IronOS/blob/662829ebd9530e83c460f7c5dfcd2d0ea8ff401e/source/Core/Src/Settings.cpp
MAX_TEMP_C = 450
MAX_TEMP_F = 850
MIN_TEMP_C =  10
MIN_TEMP_F =  60
MIN_BOOST_TEMP_C = 250
MIN_BOOST_TEMP_F = 480
MAX_SLEEP_TEMP_C = 300
MAX_SLEEP_TEMP_F = 570

value_limits = {
    "00000000-0000-1000-8000-00805f9b34fb":    [0, 1],                   # Set 1 to save
    "00000001-0000-1000-8000-00805f9b34fb":    [MIN_TEMP_C, MAX_TEMP_F], # SolderingTemp
    "00000002-0000-1000-8000-00805f9b34fb":    [MIN_TEMP_C, MAX_TEMP_F], # SleepTemp
    "00000003-0000-1000-8000-00805f9b34fb":    [0, 15],                  # SleepTime
    "00000004-0000-1000-8000-00805f9b34fb":    [0, 4],                   # MinDCVoltageCells
    "00000005-0000-1000-8000-00805f9b34fb":    [24, 38],                 # MinVoltageCells
    "00000006-0000-1000-8000-00805f9b34fb":    [90, 220],                # QCIdealVoltage
    "00000007-0000-1000-8000-00805f9b34fb":    [0, 2],                   # OrientationMode
    "00000008-0000-1000-8000-00805f9b34fb":    [0, 9],                   # Sensitivity
    "00000009-0000-1000-8000-00805f9b34fb":    [0, 1],                   # AnimationLoop
    "0000000a-0000-1000-8000-00805f9b34fb":    [0, 3],                   # AnimationSpeed
    "0000000b-0000-1000-8000-00805f9b34fb":    [0, 3],                   # AutoStartMode
    "0000000c-0000-1000-8000-00805f9b34fb":    [0, 60],                  # ShutdownTime
    "0000000d-0000-1000-8000-00805f9b34fb":    [0, 1],                   # CoolingTempBlink
    "0000000e-0000-1000-8000-00805f9b34fb":    [0, 1],                   # DetailedIDLE
    "0000000f-0000-1000-8000-00805f9b34fb":    [0, 1],                   # DetailedSoldering
    "00000010-0000-1000-8000-00805f9b34fb":    [0, 1],                   # TemperatureInF
    "00000011-0000-1000-8000-00805f9b34fb":    [0, 1],                   # DescriptionScrollSpeed
    "00000012-0000-1000-8000-00805f9b34fb":    [0, 2],                   # LockingMode
    "00000013-0000-1000-8000-00805f9b34fb":    [0, 99],                  # KeepAwakePulse
    "00000014-0000-1000-8000-00805f9b34fb":    [1, 9],                   # KeepAwakePulseWait
    "00000015-0000-1000-8000-00805f9b34fb":    [1, 9],                   # KeepAwakePulseDuration
    "00000016-0000-1000-8000-00805f9b34fb":    [360, 900],               # VoltageDiv
    "00000017-0000-1000-8000-00805f9b34fb":    [0, MAX_TEMP_F],          # BoostTemp
    "00000018-0000-1000-8000-00805f9b34fb":    [100, 2500],              # CalibrationOffset
    "00000019-0000-1000-8000-00805f9b34fb":    [0, 220],                 # PowerLimit
    "0000001a-0000-1000-8000-00805f9b34fb":    [0, 1],                   # ReverseButtonTempChangeEnabled
    "0000001b-0000-1000-8000-00805f9b34fb":    [5, 90],                  # TempChangeLongStep
    "0000001c-0000-1000-8000-00805f9b34fb":    [1, 50],                  # TempChangeShortStep
    "0000001d-0000-1000-8000-00805f9b34fb":    [0, 9],                   # HallEffectSensitivity
    "0000001e-0000-1000-8000-00805f9b34fb":    [0, 9],                   # AccelMissingWarningCounter
    "0000001f-0000-1000-8000-00805f9b34fb":    [0, 9],                   # PDMissingWarningCounter
    "00000020-0000-1000-8000-00805f9b34fb":    [0, 0xFFFF],              # UILanguage
    "00000021-0000-1000-8000-00805f9b34fb":    [0, 50],                  # PDNegTimeout
    "00000022-0000-1000-8000-00805f9b34fb":    [0, 1],                   # OLEDInversion
    "00000023-0000-1000-8000-00805f9b34fb":    [0, 99],                  # OLEDBrightness
    "00000024-0000-1000-8000-00805f9b34fb":    [0, 5],                   # LOGOTime
}
