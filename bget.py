import asyncio
import logging
from bleak import BleakClient
from bleak import BleakScanner
import struct
import os
import websockets
import json

LOG_LEVEL = os.environ.get('LOG_LEVEL', 'INFO').upper()
logging.basicConfig(level=LOG_LEVEL)

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
        values_map = {}
        for crx in service.characteristics:
            value = await client.read_gatt_char(crx.handle)
            number = struct.unpack('<H', value)[0]
            values_map[crx.uuid] = number
        return values_map
    
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

start_server = websockets.serve(hello, 'localhost', 12999) #type: ignore
asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()