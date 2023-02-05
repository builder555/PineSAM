import asyncio
import logging
from time import sleep
from bleak import BleakClient
from bleak import BleakScanner
import struct
import os
import websockets
import json

LOG_LEVEL = os.environ.get('LOG_LEVEL', 'INFO').upper()
logging.basicConfig(level=LOG_LEVEL)


settings_map = {
    '00000001-0000-1000-8000-00805f9b34fb': 'set_temperature',
    '00000017-0000-1000-8000-00805f9b34fb': 'BoostTemperature',
    '0000000b-0000-1000-8000-00805f9b34fb': 'AutoStart',
    '0000001c-0000-1000-8000-00805f9b34fb': 'TempChangeShortStep',
    '0000001b-0000-1000-8000-00805f9b34fb': 'TempChangeLongStep',
    '00000005-0000-1000-8000-00805f9b34fb': 'MinVolCell', #x10
    '00000006-0000-1000-8000-00805f9b34fb': 'QCMaxVoltage', #x10
    '00000021-0000-1000-8000-00805f9b34fb': 'PDNegTimeout', 
    '00000004-0000-1000-8000-00805f9b34fb': 'DCInCutoff',
    '00000012-0000-1000-8000-00805f9b34fb': 'LockingMode',
    '00000008-0000-1000-8000-00805f9b34fb': 'MotionSensitivity',
    '00000002-0000-1000-8000-00805f9b34fb': 'SleepTemperature',
    '00000003-0000-1000-8000-00805f9b34fb': 'SleepTimeout', #x10
    '0000000c-0000-1000-8000-00805f9b34fb': 'ShutdownTimeout',
    '00000010-0000-1000-8000-00805f9b34fb': 'TemperatureUnit', # 0 = C, 1 = F
    '00000007-0000-1000-8000-00805f9b34fb': 'DisplayRotation',
    '0000000d-0000-1000-8000-00805f9b34fb': 'CooldownBlink',
    '00000011-0000-1000-8000-00805f9b34fb': 'ScrollingSpeed',
    '0000001a-0000-1000-8000-00805f9b34fb': 'ReverseButtonTempChange',
    '0000000a-0000-1000-8000-00805f9b34fb': 'AnimSpeed',
    '00000023-0000-1000-8000-00805f9b34fb': 'Brightness',
    '00000022-0000-1000-8000-00805f9b34fb': 'ColourInversion',
    '00000024-0000-1000-8000-00805f9b34fb': 'LOGOTime',
    '0000000e-0000-1000-8000-00805f9b34fb': 'AdvancedIdle',
    '0000000f-0000-1000-8000-00805f9b34fb': 'AdvancedSoldering',
    '00000019-0000-1000-8000-00805f9b34fb': 'PowerLimit',
    '00000025-0000-1000-8000-00805f9b34fb': 'CalibrateCJC',
    '00000013-0000-1000-8000-00805f9b34fb': 'PowerPulsePower',
    '00000014-0000-1000-8000-00805f9b34fb': 'PowerPulseWait',
    '00000015-0000-1000-8000-00805f9b34fb': 'PowerPulseDuration',
    '00000009-0000-1000-8000-00805f9b34fb': 'BLEEnabled', # maybe??
    # 00000016-0000-1000-8000-00805f9b34fb - VoltageCalibration?
    # '00000000-0000-1000-8000-00805f9b34fb': '', #save settings when written to?
    # '00000018-0000-1000-8000-00805f9b34fb': '',
    # '0000001e-0000-1000-8000-00805f9b34fb': '',
    # '00000020-0000-1000-8000-00805f9b34fb': '',
    # '00000009-0000-1000-8000-00805f9b34fb': '',
    # '0000001d-0000-1000-8000-00805f9b34fb': '',
    # '0000001f-0000-1000-8000-00805f9b34fb': '',
}
values_map = {}

async def detect_pinecil():
    logging.info('Detecting Pinecil...')
    devices = await BleakScanner.discover()
    for d in devices:
        if d.name is not None and 'pinecil' in d.name.lower():
            logging.info('Found Pinecil at %s', d.address)
            return d.address
    logging.error('Pinecil not found')
    raise Exception('Pinecil not found')

async def print_settings():
    address = await detect_pinecil()
    async with BleakClient(address) as client:
        await client.connect()
        svcs = client.services
        for service in svcs:
            if service.uuid != settings_service_uuid:
                continue
            while True:
                printed = False
                # go to top of screen
                print('\033[0;0H', end='')
                for crx in service.characteristics:
                    value = await client.read_gatt_char(crx.handle)
                    number = struct.unpack('<H', value)[0]
                    if not crx.uuid in values_map:
                        values_map[crx.uuid] = None
                    if crx.uuid in settings_map:
                        name = settings_map[crx.uuid]
                    else:
                        name = crx.uuid
                    if values_map[crx.uuid] != value:
                        highlight = '\033[1;31m'
                        end_highlight = '\033[0m'
                    else:
                        highlight = ''
                        end_highlight = ''
                    values_map[crx.uuid] = value
                    print(f'{highlight}{name:<37} - {number:<8}{end_highlight}', end=' ' if not printed else '\n')
                    printed = not printed
                sleep(5)

# asyncio.run(print_settings())

class Pinecil:

    def __init__(self):
        self.address = None
        self.settings_service_uuid = 'f6d75f91-5a10-4eba-a233-47d3f26a907f'

    async def __detect(self):
        logging.info('Detecting Pinecil...')
        devices = await BleakScanner.discover()
        for d in devices:
            if d.name is not None and 'pinecil' in d.name.lower():
                logging.info('Found Pinecil at %s', d.address)
                return d.address
        logging.error('Pinecil not found')
        raise Exception('Pinecil not found')

    async def get_all_settings(self):
        if self.address is None:
            self.address = await self.__detect()
        async with BleakClient(self.address) as client:
            await client.connect()
            settings = await self.__read_settings(client)
            return settings
    
    async def __read_settings(self, client):
        service = client.services.get_service(self.settings_service_uuid)
        for crx in service.characteristics:
            value = await client.read_gatt_char(crx.handle)
            number = struct.unpack('<H', value)[0]
            values_map[crx.uuid] = number
        return values_map
    
# async def main():
#     pinecil = Pinecil()
#     settings = await pinecil.get_all_settings()
#     print(json.dumps(settings, indent=2))

# asyncio.run(main())

pinecil = Pinecil()

async def handle_message(websocket, message):
    settings = await pinecil.get_all_settings()
    if message == 'GET_ALL':
        response = json.dumps(settings)
    elif message == 'SET_ONE':
        print("SETTING VALUE")
        response = 'ACK'
    else:
        response = 'INVALID COMMAND'

    await websocket.send(response)

async def hello(websocket, path):
    message = await websocket.recv()
    await handle_message(websocket, message)

start_server = websockets.serve(hello, 'localhost', 12999)
asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()