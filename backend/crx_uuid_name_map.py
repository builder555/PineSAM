bulk_data_names = {
  '00000001-0000-1000-8000-00805f9b34fb': 'BulkData',
  '00000002-0000-1000-8000-00805f9b34fb': 'Accelerometer',
  '00000003-0000-1000-8000-00805f9b34fb': 'Build',
  '00000004-0000-1000-8000-00805f9b34fb': 'DeviceID',
}

names_v220 = {
  "00000000-0000-1000-8000-00805f9b34fb": "save_to_flash",
  "00000001-0000-1000-8000-00805f9b34fb": "SetTemperature",
  "00000002-0000-1000-8000-00805f9b34fb": "SleepTemperature",
  "00000003-0000-1000-8000-00805f9b34fb": "SleepTimeout",
  "00000004-0000-1000-8000-00805f9b34fb": "DCInCutoff",
  "00000005-0000-1000-8000-00805f9b34fb": "MinVolCell",
  "00000006-0000-1000-8000-00805f9b34fb": "QCMaxVoltage",
  "00000007-0000-1000-8000-00805f9b34fb": "DisplayRotation",
  "00000008-0000-1000-8000-00805f9b34fb": "MotionSensitivity",
  "00000009-0000-1000-8000-00805f9b34fb": "AnimLoop",
  "0000000a-0000-1000-8000-00805f9b34fb": "AnimSpeed",
  "0000000b-0000-1000-8000-00805f9b34fb": "AutoStart",
  "0000000c-0000-1000-8000-00805f9b34fb": "ShutdownTimeout",
  "0000000d-0000-1000-8000-00805f9b34fb": "CooldownBlink",
  "0000000e-0000-1000-8000-00805f9b34fb": "AdvancedIdle",
  "0000000f-0000-1000-8000-00805f9b34fb": "AdvancedSoldering",
  "00000010-0000-1000-8000-00805f9b34fb": "TemperatureUnit",
  "00000011-0000-1000-8000-00805f9b34fb": "ScrollingSpeed",
  "00000012-0000-1000-8000-00805f9b34fb": "LockingMode",
  "00000013-0000-1000-8000-00805f9b34fb": "PowerPulsePower",
  "00000014-0000-1000-8000-00805f9b34fb": "PowerPulseWait",
  "00000015-0000-1000-8000-00805f9b34fb": "PowerPulseDuration",
  "00000016-0000-1000-8000-00805f9b34fb": "VoltageCalibration",
  "00000017-0000-1000-8000-00805f9b34fb": "BoostTemperature",
  "00000018-0000-1000-8000-00805f9b34fb": "CalibrationOffset",
  "00000019-0000-1000-8000-00805f9b34fb": "PowerLimit",
  "0000001a-0000-1000-8000-00805f9b34fb": "ReverseButtonTempChange",
  "0000001b-0000-1000-8000-00805f9b34fb": "TempChangeLongStep",
  "0000001c-0000-1000-8000-00805f9b34fb": "TempChangeShortStep",
  "0000001d-0000-1000-8000-00805f9b34fb": "HallEffectSensitivity",
  "0000001e-0000-1000-8000-00805f9b34fb": "AccelMissingWarningCounter",
  "0000001f-0000-1000-8000-00805f9b34fb": "PDMissingWarningCounter",
  "00000020-0000-1000-8000-00805f9b34fb": "UILanguage",
  "00000021-0000-1000-8000-00805f9b34fb": "PDNegTimeout",
  "00000022-0000-1000-8000-00805f9b34fb": "ColourInversion",
  "00000023-0000-1000-8000-00805f9b34fb": "Brightness",
  "00000024-0000-1000-8000-00805f9b34fb": "LOGOTime",
  "00000025-0000-1000-8000-00805f9b34fb": "CalibrateCJC",
}

def reduce_idx(idx: str) -> str:
  parts = idx.split("-")
  first_group_as_number = int(parts[0],16)
  # 0xffff ensures -1 becomes 0x0000ffff:
  new_first_group_as_hex = f"{first_group_as_number-1 & 0xffff:08x}"
  return '-'.join([new_first_group_as_hex] + parts[1:])

names_v221 = {
  **{reduce_idx(k): v for k, v in names_v220.items()},
  "00000025-0000-1000-8000-00805f9b34fb": "BLEEnabled",
  "0000fffe-0000-1000-8000-00805f9b34fb": "SettingsReset",
}
