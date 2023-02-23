import pytest
from unittest.mock import AsyncMock, MagicMock, patch
from pinecil_ble import Pinecil
from test_data import settings as fake_settings
from test_data import live_data as fake_live_data

@pytest.fixture
def mocked_settings():
    return fake_settings

@pytest.fixture
def mocked_live_data():
    return fake_live_data

@pytest.fixture
def mock_ble(mocked_settings, mocked_live_data):

    async def get_characteristics(uuid):
        if uuid == 'f6d75f91-5a10-4eba-a233-47d3f26a907f':
            return mocked_settings
        if uuid == 'd85efab4-168e-4a71-affd-33e27f9bc533':
            return mocked_live_data
        return []
    async def read_crx(a): 
        return a.raw_value

    ble = MagicMock()
    ble.is_connected = False
    ble.get_characteristics = AsyncMock(side_effect=get_characteristics)
    ble.ensure_connected = AsyncMock()
    ble.read_characteristic = read_crx
    return ble

def test_device_not_connected_after_initializing(mock_ble):
    with patch('pinecil_ble.BLE', return_value=mock_ble):
        pinecil = Pinecil()
        assert pinecil.is_connected == False
        
@pytest.mark.asyncio
async def test_after_connecting_device_loads_settings_ble_characteristics(mock_ble):
    with patch('pinecil_ble.BLE', return_value=mock_ble):
        pinecil = Pinecil()
        await pinecil.connect()
        assert Method(mock_ble.get_characteristics).was_called_with('f6d75f91-5a10-4eba-a233-47d3f26a907f')

@pytest.mark.asyncio
async def test_read_all_settings_from_v2_21(mock_ble, mocked_settings):
    with patch('pinecil_ble.BLE', return_value=mock_ble):
        pinecil = Pinecil()
        await pinecil.connect()
        settings = await pinecil.get_all_settings()
        assert settings['SetTemperature'] == mocked_settings[0].expected_value
        assert settings['SleepTemperature'] == mocked_settings[1].expected_value
        assert settings['SleepTimeout'] == mocked_settings[2].expected_value
        assert settings['DCInCutoff'] == mocked_settings[3].expected_value
        assert settings['MinVolCell'] == mocked_settings[4].expected_value
        assert settings['QCMaxVoltage'] == mocked_settings[5].expected_value
        assert settings['DisplayRotation'] == mocked_settings[6].expected_value
        assert settings['MotionSensitivity'] == mocked_settings[7].expected_value
        assert settings['AnimLoop'] == mocked_settings[8].expected_value
        assert settings['AnimSpeed'] == mocked_settings[9].expected_value
        assert settings['AutoStart'] == mocked_settings[10].expected_value
        assert settings['ShutdownTimeout'] == mocked_settings[11].expected_value
        assert settings['CooldownBlink'] == mocked_settings[12].expected_value
        assert settings['AdvancedIdle'] == mocked_settings[13].expected_value
        assert settings['AdvancedSoldering'] == mocked_settings[14].expected_value
        assert settings['TemperatureUnit'] == mocked_settings[15].expected_value
        assert settings['ScrollingSpeed'] == mocked_settings[16].expected_value
        assert settings['LockingMode'] == mocked_settings[17].expected_value
        assert settings['PowerPulsePower'] == mocked_settings[18].expected_value
        assert settings['PowerPulseWait'] == mocked_settings[19].expected_value
        assert settings['PowerPulseDuration'] == mocked_settings[20].expected_value
        assert settings['VoltageCalibration'] == mocked_settings[21].expected_value
        assert settings['BoostTemperature'] == mocked_settings[22].expected_value
        assert settings['CalibrationOffset'] == mocked_settings[23].expected_value
        assert settings['PowerLimit'] == mocked_settings[24].expected_value
        assert settings['ReverseButtonTempChange'] == mocked_settings[25].expected_value
        assert settings['TempChangeLongStep'] == mocked_settings[26].expected_value
        assert settings['TempChangeShortStep'] == mocked_settings[27].expected_value
        assert settings['HallEffectSensitivity'] == mocked_settings[28].expected_value
        assert settings['AccelMissingWarningCounter'] == mocked_settings[29].expected_value
        assert settings['PDMissingWarningCounter'] == mocked_settings[30].expected_value
        assert settings['UILanguage'] == mocked_settings[31].expected_value
        assert settings['PDNegTimeout'] == mocked_settings[32].expected_value
        assert settings['ColourInversion'] == mocked_settings[33].expected_value
        assert settings['Brightness'] == mocked_settings[34].expected_value

@pytest.mark.asyncio
async def test_reading_settings_while_disconnected_reconnects(mock_ble):
    with patch('pinecil_ble.BLE', return_value=mock_ble):
        pinecil = Pinecil()
        await pinecil.get_all_settings()
        assert mock_ble.ensure_connected.called

@pytest.mark.asyncio
async def test_get_live_data(mock_ble, mocked_live_data):
    with patch('pinecil_ble.BLE', return_value=mock_ble):
        pinecil = Pinecil()
        await pinecil.connect()
        live_data = await pinecil.get_live_data()
        assert live_data['LiveTemp'] == mocked_live_data[0].expected_value
        assert live_data['Voltage'] == mocked_live_data[1].expected_value
        assert live_data['HandleTemp'] == mocked_live_data[2].expected_value
        assert live_data['OperatingMode'] == mocked_live_data[3].expected_value
        assert live_data['Watts'] == mocked_live_data[4].expected_value

@pytest.mark.asyncio
async def test_reading_live_data_while_disconnected_reconnects(mock_ble):
    with patch('pinecil_ble.BLE', return_value=mock_ble):
        pinecil = Pinecil()
        await pinecil.get_live_data()
        assert mock_ble.ensure_connected.called

def test_read_all_settings_from_v2_20():
    pass

def test_update_one_setting_at_a_time():
    pass

def test_updating_setting_with_invalid_value_fails():
    pass

def test_can_save_changes_to_flash():
    pass

def test_get_unique_device_name():
    pass



class Method:
    def __init__(self, mocked_func):
        self.mocked_func = mocked_func
        self.mock_calls = mocked_func.mock_calls
    def was_called_with(self, *args):
        for call in self.mock_calls:
            if len(call) < 2:
                continue
            if len(call[1]) < 1:
                continue
            if call[1][0]==args[0]:
                return True
        raise AssertionError(f'No call to {self.mocked_func} with args {args}:\n {self.mock_calls}')
