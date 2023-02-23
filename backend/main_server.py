import asyncio
import logging
import os
import websockets
import websockets.exceptions
import json
from ble import DeviceNotFoundException
from pinecil_ble import Pinecil
from pinecil_ble import InvalidSettingException
from pinecil_ble import ValueOutOfRangeException

LOG_LEVEL = os.environ.get('LOG_LEVEL', 'INFO').upper()
timestamp_format = '%H:%M:%S'
logging.basicConfig(level=LOG_LEVEL, format='%(asctime)s.%(msecs)03d::%(levelname)s::%(message)s', datefmt=timestamp_format)

pinecil = Pinecil()

def read_app_version():
    with open('../version.txt') as f:
        return f.read().strip()

async def process_command(command: str, payload: dict) -> dict:
    if not pinecil.is_connected:
        await pinecil.connect()
    if command == 'GET_SETTINGS':
        settings = await pinecil.get_all_settings()
        return {'status': 'OK', 'payload': settings}
    if command == 'UPDATE_SETTING':
        logging.info("SETTING VALUE")
        await pinecil.set_one_setting(payload['name'], payload['value'])
        if payload.get('save'):
            logging.info("SAVING TO FLASH")
            await pinecil.save_to_flash()
        return {'status': 'OK'}
    if command == 'GET_INFO':
        info = await pinecil.get_info()
        info['app_version'] = read_app_version()
        return {'status': 'OK', 'payload': info}
    return {'status': 'ERROR', 'message': 'Unknown command'}

async def handle_message(websocket, data):
    logging.info(f'Got message: {data}') 
    json_data = json.loads(data)
    command, payload = json_data['command'], json_data.get('payload', {})
    try:
        response = await process_command(command, payload)
        logging.info(f'Sending response')
    except (
            InvalidSettingException,
            DeviceNotFoundException,
            ValueOutOfRangeException,
            ) as e:
        logging.warning(e.message)
        response = {'status': 'ERROR', 'message': e.message}
    await websocket.send(json.dumps({**response, 'command': command}))

sockets = set()

async def ws_handler(websocket):
    try:
        sockets.add(websocket)
        while True:
            message = await websocket.recv()
            await handle_message(websocket, message)
    except websockets.exceptions.ConnectionClosed:
        logging.info('Connection closed')
        sockets.remove(websocket)

async def main():
    async with websockets.serve(ws_handler, '0.0.0.0', 12999): #type: ignore
        await asyncio.Future()

if __name__ == '__main__':
    asyncio.run(main())
