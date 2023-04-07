from typing import List, Tuple, Dict
import struct
import logging
import asyncio
from pinecil_setting_limits import value_limits
from pinecil_setting_limits import temperature_limits
from crx_uuid_name_map import names_v220, names_v221beta1, names_v221beta2, bulk_data_names_v220, bulk_data_names_v221beta2
from ble import BleakGATTCharacteristic
from ble import BLE
import time

class ValueOutOfRangeException(Exception):
    message = 'Value out of range'

class InvalidSettingException(Exception):
    message = 'Invalid setting'


class SettingNameToUUIDMap:
    def __init__(self):
        self.names = names_v220

    def set_version(self, version: str):
        names = {
            '2.20': names_v220,
            '2.21beta1': names_v221beta1,
            '2.21beta2': names_v221beta2,
        }
        self.names = names.get(version, names_v220)

    def get_name(self, uuid: str) -> str:
        return self.names.get(uuid, uuid)
    
    def get_uuid(self, name: str) -> str:
        return next((k for k, v in self.names.items() if v == name), name)

class BulkDataToUUIDMap:
    def __init__(self):
        self.names = bulk_data_names_v220

    def set_version(self, version: str):
        names = {
            '2.20': bulk_data_names_v220,
            '2.21beta1': bulk_data_names_v220,
            '2.21beta2': bulk_data_names_v221beta2,
        }
        self.names = names.get(version, names_v220)

    def get_name(self, uuid: str) -> str:
        return self.names.get(uuid, uuid)
    
    def get_uuid(self, name: str) -> str:
        return next((k for k, v in self.names.items() if v == name), name)


class Pinecil:

    def __init__(self):
        self.ble = BLE(name='pinecil')
        self.settings_uuid: str
        self.bulk_data_uuid: str
        self.temp_unit_crx: str = 'TemperatureUnit'
        self.settings_map = SettingNameToUUIDMap()
        self.bulk_data_map = BulkDataToUUIDMap()
        self.crx_settings: List[BleakGATTCharacteristic] = []
        self.crx_bulk_data: BleakGATTCharacteristic
        self.bulk_data_to_read: str = 'BulkData'
        self.is_initialized = False
        self.is_getting_settings = False
        self.__last_read_settings = {}
        self.__last_read_settings_time = 0

    @property
    def is_connected(self):
        return self.ble.is_connected and self.is_initialized

    async def __set_ble_uuids_based_on_version(self):
        # this is just a hack until the version is exposed in the settings
        uuid_settings_pre_221 = 'f6d75f91-5a10-4eba-a233-47d3f26a907f'
        uuid_settings_221beta2 = 'f6d80000-5a10-4eba-aa55-33e27f9bc533'
        uuid_bulk_data_pre_221 = '9eae1adb-9d0d-48c5-a6e7-ae93f0ea37b0'
        uuid_bulk_data_221beta2 = '9eae1000-9d0d-48c5-aa55-33e27f9bc533'
        services = await self.ble.get_services()
        if uuid_settings_221beta2 in services:
            self.settings_uuid = uuid_settings_221beta2
            self.bulk_data_uuid = uuid_bulk_data_221beta2
            self.settings_map.set_version('2.21beta2')
            self.bulk_data_map.set_version('2.21beta2')
            return
        crx_settings = await self.ble.get_characteristics(uuid_settings_pre_221)
        for crx in crx_settings:
            if crx.uuid == '0000ffff-0000-1000-8000-00805f9b34fb':
                self.settings_map.set_version('2.21beta1')
                self.bulk_data_map.set_version('2.21beta1')
                break
        else:
            self.settings_map.set_version('2.20')
            self.bulk_data_map.set_version('2.20')
        self.settings_uuid = uuid_settings_pre_221
        self.bulk_data_uuid = uuid_bulk_data_pre_221

    async def connect(self):
        await self.ble.ensure_connected()
        await self.__set_ble_uuids_based_on_version()

        self.crx_settings = await self.ble.get_characteristics(self.settings_uuid)
        bulk_crx = await self.ble.get_characteristics(self.bulk_data_uuid)
        for crx in bulk_crx:
            if crx.uuid == self.bulk_data_map.get_uuid(self.bulk_data_to_read):
                self.crx_bulk_data = crx
                break
        self.unique_id = await self.__get_pinecil_id()
        self.is_initialized = True
        
    async def __read_setting(self, crx: BleakGATTCharacteristic) -> Tuple[str, int]:
        raw_value = await self.ble.read_characteristic(crx)
        number = struct.unpack('<H', raw_value)[0]
        return self.settings_map.get_name(crx.uuid), number

    async def __get_pinecil_id(self):
        try:
            characteristics = await self.ble.get_characteristics(self.bulk_data_uuid)
            for crx in characteristics:
                if crx.uuid == self.bulk_data_map.get_uuid('DeviceID'):
                    raw_value = await self.ble.read_characteristic(crx)
                    n = struct.unpack('<Q',raw_value)[0]
                    # using algorithm from here:
                    # https://github.com/Ralim/IronOS/commit/eb5d6ea9fd6acd221b8880650728e13968e54d3d
                    unique_id = ((n & 0xFFFFFFFF) ^ ((n >> 32) & 0xFFFFFFFF))
                    return f'{unique_id:X}'
        except:
            return ''

    async def get_all_settings(self) -> Dict[str, int]:
        logging.info('REQUEST FOR SETTINGS')
        while self.is_getting_settings:
            await asyncio.sleep(0.5)
        if time.time() - self.__last_read_settings_time < 2:
            return self.__last_read_settings
        try:
            logging.info(f'Reading all settings')
            self.is_getting_settings = True
            if not self.is_connected:
                await self.connect()
            tasks = [asyncio.ensure_future(self.__read_setting(crx)) for crx in self.crx_settings]
            results = await asyncio.gather(*tasks)
            settings = dict(results)
            logging.info(f'Reading all settings DONE')
            self.__last_read_settings = settings
            self.__last_read_settings_time = time.time()
            return settings
        except Exception as e:
            raise e
        finally:
            self.is_getting_settings = False

    async def __ensure_valid_temperature(self, setting, temperature):
        characteristics = await self.ble.get_characteristics(self.settings_uuid)
        temp_uuid = self.settings_map.get_uuid(self.temp_unit_crx)
        for crx in characteristics:
            if crx.uuid == temp_uuid:
                raw_value = await self.ble.read_characteristic(crx)
                temp_unit = struct.unpack('<H', raw_value)[0]
                within_limit = temperature_limits[setting][temp_unit]
                if not within_limit(temperature):
                    logging.warning(f'Temp. {temperature} is out of range for setting {setting}')
                    raise ValueOutOfRangeException
                break

    async def set_one_setting(self, setting, value):
        ensure_setting_exists(setting)
        ensure_setting_value_within_limits(setting, value)
        if not self.is_connected:
            await self.connect()
        if setting in temperature_limits:
            await self.__ensure_valid_temperature(setting, value)
        logging.info(f'Setting {value} ({type(value)}) to {setting}')
        uuid = self.settings_map.get_uuid(setting)
        for crx in self.crx_settings:
            if crx.uuid == uuid:
                value = struct.pack('<H', value)
                await self.ble.write_characteristic(crx, bytearray(value))
                break
        else:
            raise Exception('Setting not found')

    async def save_to_flash(self):
        await self.set_one_setting('save_to_flash', 1)

    async def get_info(self):
        return {
            'name': f'Pinecil-{self.unique_id}',
            'id': self.unique_id,
        }

    async def __read_live_data(self, crx: BleakGATTCharacteristic) -> Dict[str, int]:
        raw_value = await self.ble.read_characteristic(crx)
        num_of_values = len(raw_value) >> 2 # divide by 4
        values = struct.unpack(f'<{num_of_values}I', raw_value)
        values_map = [
            "LiveTemp",
            "SetTemp",
            "Voltage",
            "HandleTemp",
            "PWMLevel",
            "PowerSource",
            "TipResistance",
            "Uptime",
            "MovementTime",
            "MaxTipTempAbility",
            "uVoltsTip",
            "HallSensor",
            "OperatingMode",
            "Watts",
        ]
        return dict(zip(values_map, values))

    async def get_live_data(self) -> Dict[str, int]:
        logging.debug(f'GETTING ALL LIVE VALUES')
        if not self.is_connected:
            await self.connect()
        values = await self.__read_live_data(self.crx_bulk_data)
        logging.debug(f'GETTING ALL LIVE VALUES DONE')
        return values


def ensure_setting_exists(name: str):
    if name not in names_v220.values() and name not in names_v221beta1.values():
        logging.warning(f'Setting {name} does not exist')
        raise InvalidSettingException

def ensure_setting_value_within_limits(name: str, value: int):
    min_val, max_val = value_limits[name]
    if not min_val <= value <= max_val:
        logging.warning(f'Value {value} is out of range for setting {name} ({min_val}-{max_val})')
        raise ValueOutOfRangeException
