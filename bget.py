import asyncio
import logging
import os
import websockets
import json
from pinecil_ble import Pinecil

LOG_LEVEL = os.environ.get('LOG_LEVEL', 'INFO').upper()
logging.basicConfig(level=LOG_LEVEL)

pinecil = Pinecil()

async def handle_message(websocket, data):
    logging.info(f'Got message: {data}')
    json_data = json.loads(data)
    command, payload = json_data['command'], json_data.get('payload', None)
    if command == 'GET_SETTINGS':
        settings = await pinecil.get_all_settings()
        response = json.dumps(settings)
    elif command == 'UPDATE_SETTING':
        logging.info("SETTING VALUE")
        await pinecil.set_one_setting(payload['uuid'], payload['value'])
        if payload.get('save'):
            logging.info("SAVING TO FLASH")
            await pinecil.set_one_setting('00000000-0000-1000-8000-00805f9b34fb', 1)
        response = json.dumps({'status': 'OK'})
    else:
        response = json.dumps({'status': 'ERROR', 'message': 'Unknown command'})

    await websocket.send(response)

async def hello(websocket, path):
    message = await websocket.recv()
    await handle_message(websocket, message)

start_server = websockets.serve(hello, 'localhost', 12999) #type: ignore
asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()
