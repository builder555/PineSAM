import logging
from typing import List
from bleak import BleakClient
from bleak import BleakScanner
from bleak.exc import BleakDeviceNotFoundError
from bleak.backends.characteristic import BleakGATTCharacteristic

class DeviceNotFoundException(Exception):
    message = 'Device not found'


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

    async def ensure_connected(self):
        try:
            if self.is_connected:
                return
            if not self.address:
                await self.__detect_device_address()
            self.client = BleakClient(self.address)
            await self.client.connect()
        except BleakDeviceNotFoundError:
            logging.info(f'Could not find device "{self.device_name}" at "{self.address}"')
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
        await self.ensure_connected()
        service = self.client.services.get_service(service_uuid) #type: ignore
        if service:
            return service.characteristics
        raise Exception(f'Could not find service {service_uuid}')

    async def read_characteristic(self, handle: BleakGATTCharacteristic) -> bytes:
        await self.ensure_connected()
        return await self.client.read_gatt_char(handle) #type: ignore

    async def write_characteristic(self, handle: BleakGATTCharacteristic, value: bytes):
        await self.ensure_connected()
        logging.debug(f'Writing characteristic {handle.uuid}')
        await self.client.write_gatt_char(handle, value) #type: ignore
        logging.debug(f'Writing characteristic {handle.uuid} DONE')
    
    async def __del__(self):
        try:
            if self.client:
                await self.client.disconnect()
        except:
            pass
