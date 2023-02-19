from typing import List
import struct
import logging
import asyncio
from pinecil_setting_limits import value_limits
from pinecil_setting_limits import temperature_limits
from setting_names_map import names_v220, names_v221
from ble import BleakGATTCharacteristic
from ble import BLE

class ValueOutOfRangeException(Exception):
    message = 'Value out of range'

class InvalidSettingException(Exception):
    message = 'Invalid setting'


class SettingNameToUUIDMap:
    def __init__(self):
        self.names = names_v220

    def set_version(self, version: str):
        self.names = names_v220 if version == '2.20' else names_v221
        
    def get_name(self, uuid: str) -> str:
        return self.names.get(uuid, uuid)
    
    def get_uuid(self, name: str) -> str:
        return next((k for k, v in self.names.items() if v == name), name)


class Pinecil:

    def __init__(self):
        self.ble = BLE(name='pinecil')
        self.settings_uuid: str = 'f6d75f91-5a10-4eba-a233-47d3f26a907f'
        self.bulk_data_uuid: str = '9eae1adb-9d0d-48c5-a6e7-ae93f0ea37b0'
        self.temp_unit_crx: str = 'TemperatureUnit'
        self.names_map = SettingNameToUUIDMap()
        self.characteristics: List[BleakGATTCharacteristic] = []

    @property
    def is_connected(self):
        return self.ble.is_connected

    def __get_version(self, crxs: List[BleakGATTCharacteristic]):
        # this is just a hack until the version is exposed in the settings
        for crx in crxs:
            if crx.uuid == '0000ffff-0000-1000-8000-00805f9b34fb':
                return '2.21'
        return '2.20'
        
    async def connect(self):
        await self.ble.ensure_connected()
        self.characteristics = await self.ble.get_characteristics(self.settings_uuid)
        self.names_map.set_version(self.__get_version(self.characteristics))
        self.unique_id = await self.__get_pinecil_id()
        
    async def __read_setting(self, crx: BleakGATTCharacteristic) -> tuple[str, int]:
        raw_value = await self.ble.read_characteristic(crx)
        number = struct.unpack('<H', raw_value)[0]
        return self.names_map.get_name(crx.uuid), number

    async def __get_pinecil_id(self):
        try:
            characteristics = await self.ble.get_characteristics(self.bulk_data_uuid)
            for crx in characteristics:
                if crx.uuid == '00000004-0000-1000-8000-00805f9b34fb':
                    raw_value = await self.ble.read_characteristic(crx)
                    n = struct.unpack('<Q',raw_value)[0]
                    # using algorithm from here:
                    # https://github.com/Ralim/IronOS/commit/eb5d6ea9fd6acd221b8880650728e13968e54d3d
                    unique_id = ((n & 0xFFFFFFFF) ^ ((n >> 32) & 0xFFFFFFFF))
                    return f'{unique_id:X}'
        except:
            return ''

    async def get_all_settings(self) -> dict[str, int]:
        logging.debug(f'GETTING ALL SETTINGS')
        if not self.is_connected:
            await self.connect()
        tasks = [asyncio.ensure_future(self.__read_setting(crx)) for crx in self.characteristics]
        results = await asyncio.gather(*tasks)
        settings = dict(results)
        logging.debug(f'GETTING ALL SETTINGS DONE')
        return settings

    async def __ensure_valid_temperature(self, setting, temperature):
        characteristics = await self.ble.get_characteristics(self.settings_uuid)
        temp_uuid = self.names_map.get_uuid(self.temp_unit_crx)
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
        uuid = self.names_map.get_uuid(setting)
        for crx in self.characteristics:
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

def ensure_setting_exists(name: str):
    if name not in names_v220.values() and name not in names_v221.values():
        logging.warning(f'Setting {name} does not exist')
        raise InvalidSettingException

def ensure_setting_value_within_limits(name: str, value: int):
    min_val, max_val = value_limits[name]
    if not min_val <= value <= max_val:
        logging.warning(f'Value {value} is out of range for setting {name} ({min_val}-{max_val})')
        raise ValueOutOfRangeException
