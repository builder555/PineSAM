import asyncio
import logging
import os
import websockets
import json
from pinecil_ble import Pinecil

LOG_LEVEL = os.environ.get('LOG_LEVEL', 'INFO').upper()
timestamp_format = '%H:%M:%S'
logging.basicConfig(level=LOG_LEVEL, format='%(asctime)s.%(msecs)03d::%(levelname)s::%(message)s', datefmt=timestamp_format)

pinecil = Pinecil()

async def handle_message(websocket, data):
    logging.info(f'Got message: {data}') 
    json_data = json.loads(data)
    command, payload = json_data['command'], json_data.get('payload', None)
    if command == 'GET_SETTINGS':
        settings = await pinecil.get_all_settings()
        response = {'status': 'OK', 'payload': settings}
    elif command == 'UPDATE_SETTING':
        logging.info("SETTING VALUE")
        await pinecil.set_one_setting(payload['uuid'], payload['value'])
        if payload.get('save'):
            logging.info("SAVING TO FLASH")
            await pinecil.set_one_setting('00000000-0000-1000-8000-00805f9b34fb', 1)
        response = {'status': 'OK'}
    else:
        response = {'status': 'ERROR', 'message': 'Unknown command'}
    logging.info(f'Sending response')
    await websocket.send(json.dumps({**response, 'command': command}))

async def hello(websocket, path):
    while True:
        message = await websocket.recv()
        await handle_message(websocket, message)

start_server = websockets.serve(hello, 'localhost', 12999) #type: ignore
asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()
