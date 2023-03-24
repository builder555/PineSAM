import asyncio
import logging
import os
import websockets
import websockets.exceptions
import json
import requests
from ble import DeviceNotFoundException
from ble import DeviceDisconnectedException
from pinecil_ble import Pinecil
from pinecil_ble import InvalidSettingException
from pinecil_ble import ValueOutOfRangeException

LOG_LEVEL = os.environ.get('LOG_LEVEL', 'INFO').upper()
timestamp_format = '%H:%M:%S'
logging.basicConfig(level=LOG_LEVEL, format='%(asctime)s.%(msecs)03d::%(levelname)s::%(message)s', datefmt=timestamp_format)

pinecil = Pinecil()

def read_app_version():
    parent_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    with open(os.path.join(parent_dir, 'version.txt')) as f:
        return f.read().strip()

def get_latest_version():
    url = 'https://api.github.com/repos/builder555/PineSAM/releases/latest'
    release_info = requests.get(url).json()
    return release_info.get('tag_name', read_app_version()).strip('v')

def is_semver_greater(v1, v2):
    v1 = list(map(int, v1.split('.')))
    v2 = list(map(int, v2.split('.')))
    return v1 > v2

async def process_command(command: str, payload: dict) -> dict:
    if command == 'GET_APP_INFO':
        app_version = read_app_version()
        info = {
            'app_version': app_version,
            'is_new_available': is_semver_greater(get_latest_version(), app_version),
        }
        return {'status': 'OK', 'payload': info}
    while not pinecil.is_connected:
        await asyncio.sleep(0.5)
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

CLIENTS = set()

async def ws_handler(websocket):
    try:
        CLIENTS.add(websocket)
        while True:
            message = await websocket.recv()
            await handle_message(websocket, message)
    except websockets.exceptions.ConnectionClosed:
        logging.info('Connection closed')
        CLIENTS.remove(websocket)

async def send(ws, message):
    try:
        await ws.send(message)
    except websockets.exceptions.ConnectionClosed:
        pass

def broadcast(message):
    for client in CLIENTS:
        asyncio.create_task(send(client, message))

async def pinecil_monitor(stop_event: asyncio.Event):
    logging.info('Starting pinecil monitor')
    should_announce_not_found = True
    while not stop_event.is_set():
        if not pinecil.is_connected:
            logging.info('waiting for pinecil...')
            try:
                await pinecil.connect()
            except DeviceNotFoundException as e:
                logging.warning(e.message)
                response = {'status': 'ERROR', 'message': e.message}
                if should_announce_not_found:
                    broadcast(json.dumps(response))
                should_announce_not_found = False
            await asyncio.sleep(1)
            continue
        try:
            should_announce_not_found = True
            pinecil_data = await pinecil.get_live_data()
            msg = json.dumps({'command': 'LIVE_DATA', 'payload': pinecil_data, 'status': 'OK'})
            broadcast(msg)
            await asyncio.sleep(0.5)
        except DeviceDisconnectedException:
            logging.info('Pinecil disconnected')
            broadcast(json.dumps({'status': 'ERROR', 'message': 'Device disconnected'}))

async def main(stop_event = asyncio.Event()):
    tasks = [
        asyncio.create_task(pinecil_monitor(stop_event)),
        websockets.serve(ws_handler, '0.0.0.0', 12999), #type: ignore
    ]
    await asyncio.gather(*tasks)


if __name__ == '__main__':
    asyncio.run(main())
