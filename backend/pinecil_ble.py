from typing import List
import struct
import logging
import asyncio
import bleak
from bleak import BleakClient
from bleak import BleakScanner
from bleak.backends.characteristic import BleakGATTCharacteristic
from pinecil_setting_limits import value_limits
from pinecil_setting_limits import MAX_TEMP_C
from pinecil_setting_limits import MAX_TEMP_F
from pinecil_setting_limits import MIN_TEMP_C
from pinecil_setting_limits import MIN_TEMP_F
from pinecil_setting_limits import MIN_BOOST_TEMP_C
from pinecil_setting_limits import MIN_BOOST_TEMP_F
from pinecil_setting_limits import MAX_SLEEP_TEMP_C
from pinecil_setting_limits import MAX_SLEEP_TEMP_F

class DeviceNotFoundException(Exception):
    pass

class ValueOutOfRangeException(Exception):
    pass

class BLE:

    def __init__(self, name=None, address=None):
        if not name and not address:
            raise Exception('No device name or address set')
        self.address = address
        self.device_name = name
        self.client: BleakClient | None = None

    @property
    def is_connected(self):
        return self.client and self.client.is_connected

    async def __ensure_connected(self):
        try:
            if self.is_connected:
                return
            if not self.address:
                await self.__detect_device_address()
            self.client = BleakClient(self.address)
            await self.client.connect()
        except bleak.exc.BleakDeviceNotFoundError:
            raise DeviceNotFoundException

    async def __detect_device_address(self):
        logging.info(f'Detecting "{self.device_name}"...')
        devices = await BleakScanner.discover()
        for d in devices:
            if d.name is not None and self.device_name in d.name.lower():
                logging.info(f'Found {self.device_name} at {d.address}')
                self.address = d.address
                break
        else:
            raise DeviceNotFoundException
        logging.debug(f'Detecting "{self.device_name}" DONE')

    async def get_characteristics(self, service_uuid: str) -> List[BleakGATTCharacteristic]:
        await self.__ensure_connected()
        service = self.client.services.get_service(service_uuid) #type: ignore
        if service:
            return service.characteristics
        raise Exception(f'Could not find service {service_uuid}')

    async def read_characteristic(self, handle: BleakGATTCharacteristic) -> bytes:
        await self.__ensure_connected()
        return await self.client.read_gatt_char(handle) #type: ignore

    async def write_characteristic(self, handle: BleakGATTCharacteristic, value: bytes):
        await self.__ensure_connected()
        logging.debug(f'Writing characteristic {handle.uuid}')
        await self.client.write_gatt_char(handle, value) #type: ignore
        logging.debug(f'Writing characteristic {handle.uuid} DONE')
    
    async def __del__(self):
        try:
            if self.client:
                await self.client.disconnect()
        except:
            pass

temperature_limits = {
    '00000001-0000-1000-8000-00805f9b34fb':{0:[MIN_TEMP_C, MAX_TEMP_C],1:[MIN_TEMP_F, MAX_TEMP_F]},
    '00000002-0000-1000-8000-00805f9b34fb':{0:[MIN_TEMP_C,MAX_SLEEP_TEMP_C],1:[MIN_TEMP_F,MAX_SLEEP_TEMP_F]},
    '00000017-0000-1000-8000-00805f9b34fb':{0:[MIN_BOOST_TEMP_C, MAX_TEMP_C],1:[MIN_BOOST_TEMP_F, MAX_TEMP_F]},
}
class Pinecil:

    def __init__(self):
        self.ble = BLE(name='pinecil')
        self.settings_uuid: str = 'f6d75f91-5a10-4eba-a233-47d3f26a907f'
        self.temp_unit_crx_uuid: str = '00000010-0000-1000-8000-00805f9b34fb'
    
    async def __ensure_valid_temperature(self, setting, temperature):
        characteristics = await self.ble.get_characteristics(self.settings_uuid)
        for crx in characteristics:
            if crx.uuid == self.temp_unit_crx_uuid:
                raw_value = await self.ble.read_characteristic(crx)
                temp_unit = struct.unpack('<H', raw_value)[0]
                limits = temperature_limits[setting][temp_unit]
                if not limits[0] <= temperature <= limits[1]:
                    logging.warning(f'Temp. {temperature} is out of range for setting {setting} ({limits[0]}-{limits[1]})')
                    raise ValueOutOfRangeException
                break

    async def get_all_settings(self):
        logging.debug(f'GETTING ALL SETTINGS')
        characteristics = await self.ble.get_characteristics(self.settings_uuid)
        async def read_char(ble, crx):
            raw_value = await ble.read_characteristic(crx)
            number = struct.unpack('<H', raw_value)[0]
            return crx.uuid, number
        tasks = [asyncio.ensure_future(read_char(self.ble, crx)) for crx in characteristics]
        results = await asyncio.gather(*tasks)
        settings = dict(results)
        logging.debug(f'GETTING ALL SETTINGS DONE')
        return settings

    async def set_one_setting(self, setting, value):
        limits = value_limits[setting]
        if not limits[0] <= value <= limits[1]:
            logging.warning(f'Value {value} is out of range for setting {setting} ({limits[0]}-{limits[1]})')
            raise ValueOutOfRangeException
        if setting in temperature_limits:
            await self.__ensure_valid_temperature(setting, value)
        characteristics = await self.ble.get_characteristics(self.settings_uuid)
        logging.info(f'Setting {value} ({type(value)}) to {setting}')
        for crx in characteristics:
            if crx.uuid == setting:
                value = struct.pack('<H', value)
                await self.ble.write_characteristic(crx, bytearray(value))
                break
        else:
            raise Exception('Setting not found')
