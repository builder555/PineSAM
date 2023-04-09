import pytest
from unittest.mock import AsyncMock, MagicMock, patch
from pinecil_ble import Pinecil
from test_data import settings as fake_settings
from test_data import live_data as fake_live_data
from test_utils import Method

@pytest.fixture
def mocked_settings():
    return fake_settings

@pytest.fixture
def mocked_live_data():
    return fake_live_data

@pytest.fixture
def mock_ble(mocked_settings, mocked_live_data):

    async def get_characteristics(uuid):
        if uuid == 'f6d80000-5a10-4eba-aa55-33e27f9bc533':
            return mocked_settings
        if uuid == '9eae1000-9d0d-48c5-aa55-33e27f9bc533':
            return mocked_live_data
        return []
    async def read_crx(a): 
        return a.raw_value
    mock_services = [
        'f6d80000-5a10-4eba-aa55-33e27f9bc533',
        '9eae1000-9d0d-48c5-aa55-33e27f9bc533',
    ]
    ble = MagicMock()
    ble.is_connected = False
    ble.get_characteristics = AsyncMock(side_effect=get_characteristics)
    ble.get_services = AsyncMock(return_value=mock_services)
    ble.ensure_connected = AsyncMock()
    ble.read_characteristic = read_crx
    return ble

@pytest.fixture
def mock_ble_old(mocked_settings, mocked_live_data):

    async def get_characteristics(uuid):
        if uuid == 'f6d75f91-5a10-4eba-a233-47d3f26a907f':
            return mocked_settings
        if uuid == '9eae1adb-9d0d-48c5-a6e7-ae93f0ea37b0':
            return mocked_live_data
        return []
    async def read_crx(a): 
        return a.raw_value
    mock_services = [
        MagicMock(uuid='f6d75f91-5a10-4eba-a233-47d3f26a907f'),
        MagicMock(uuid='9eae1adb-9d0d-48c5-a6e7-ae93f0ea37b0'),
    ]
    ble = MagicMock()
    ble.is_connected = False
    ble.get_characteristics = AsyncMock(side_effect=get_characteristics)
    ble.get_services = AsyncMock(return_value=mock_services)
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
        assert Method(mock_ble.get_characteristics).was_called_with('f6d80000-5a10-4eba-aa55-33e27f9bc533')

@pytest.mark.asyncio
async def test_read_all_settings_from_v2_21beta2(mock_ble, mocked_settings):
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
        assert live_data["LiveTemp"] == mocked_live_data[0].expected_value[0]
        assert live_data["SetTemp"] == mocked_live_data[0].expected_value[1]
        assert live_data["Voltage"] == mocked_live_data[0].expected_value[2]
        assert live_data["HandleTemp"] == mocked_live_data[0].expected_value[3]
        assert live_data["PWMLevel"] == mocked_live_data[0].expected_value[4]
        assert live_data["PowerSource"] == mocked_live_data[0].expected_value[5]
        assert live_data["TipResistance"] == mocked_live_data[0].expected_value[6]
        assert live_data["Uptime"] == mocked_live_data[0].expected_value[7]
        assert live_data["MovementTime"] == mocked_live_data[0].expected_value[8]
        assert live_data["MaxTipTempAbility"] == mocked_live_data[0].expected_value[9]
        assert live_data["uVoltsTip"] == mocked_live_data[0].expected_value[10]
        assert live_data["HallSensor"] == mocked_live_data[0].expected_value[11]
        assert live_data["OperatingMode"] == mocked_live_data[0].expected_value[12]
        assert live_data["Watts"] == mocked_live_data[0].expected_value[13]

@pytest.mark.asyncio
async def test_get_pinecil_info(mock_ble, mocked_live_data):
    with patch('pinecil_ble.BLE', return_value=mock_ble):
        pinecil = Pinecil()
        await pinecil.connect()
        info = await pinecil.get_info()
        assert info["build"] == mocked_live_data[1].expected_value.strip('v')
        assert info["id"] == mocked_live_data[2].expected_value
        assert info["name"] == f'Pinecil-{info["id"]}'

@pytest.mark.asyncio
async def test_get_info_returns_2_20_build_for_older_versions(mock_ble_old, mocked_live_data):
    with patch('pinecil_ble.BLE', return_value=mock_ble_old):
        pinecil = Pinecil()
        await pinecil.connect()
        info = await pinecil.get_info()
        assert info["build"] == '2.20'

@pytest.mark.asyncio
async def test_reading_live_data_while_disconnected_reconnects(mock_ble):
    with patch('pinecil_ble.BLE', return_value=mock_ble):
        pinecil = Pinecil()
        await pinecil.get_live_data()
        assert mock_ble.ensure_connected.called

def test_read_all_settings_from_v2_20():
    pass

def test_read_all_settings_from_v2_21beta1():
    pass

def test_update_one_setting_at_a_time():
    pass

def test_updating_setting_with_invalid_value_fails():
    pass

def test_can_save_changes_to_flash():
    pass

def test_get_unique_device_name():
    pass

def test_requesting_all_settings_frequently_returns_cached_values():
    pass
