import asyncio
import logging
import json
import websockets
import websockets.exceptions
from websockets.typing import Data
from pinecil import DeviceNotFoundException
from pinecil import InvalidSettingException
from pinecil import ValueOutOfRangeException
from pinecil import DeviceDisconnectedException
from pinecil import Pinecil
from pinecil_monitor import PinecilFinder
from version_checker import VersionChecker


class UnknownCommandException(Exception):
    message = "Unknown command"


class CommandProcessor:
    def __init__(
        self,
        finder: PinecilFinder,
        app_version_manager: VersionChecker,
        ironos_version_manager: VersionChecker,
    ):
        self.finder = finder
        self.app_ver = app_version_manager
        self.ironos_ver = ironos_version_manager

    @property
    def pinecil(self) -> Pinecil:
        if not self.finder.selected:
            raise DeviceNotFoundException()
        if not self.finder.selected.is_connected:
            raise DeviceDisconnectedException()
        return self.finder.selected

    async def process_command(self, command: str, payload: dict) -> dict:
        if command == "GET_APP_INFO":
            return await self.get_app_info()
        elif command == "GET_SETTINGS":
            return await self.get_settings()
        elif command == "UPDATE_SETTING":
            return await self.update_setting(payload)
        elif command == "GET_INFO":
            return await self.get_info()
        else:
            raise UnknownCommandException()

    async def get_app_info(self) -> dict:
        app_version = self.app_ver.read_version()
        return {
            "status": "OK",
            "payload": {
                "app_version": app_version,
                "is_new_available": self.is_semver_greater(
                    self.app_ver.get_latest_version(), app_version
                ),
            },
        }

    async def get_settings(self) -> dict:
        settings = await self.pinecil.get_all_settings()
        return {"status": "OK", "payload": settings}

    async def update_setting(self, payload):
        await self.pinecil.set_one_setting(payload["name"], payload["value"])
        if payload.get("save"):
            await self.pinecil.save_to_flash()
        return {"status": "OK"}

    async def get_info(self) -> dict:
        info = await self.pinecil.get_info()
        latest_build = self.ironos_ver.get_latest_version()
        return {
            "status": "OK",
            "payload": {
                **info,
                "latest_build": latest_build,
                "is_new_build_available": self.is_semver_greater(
                    latest_build, info["build"]
                ),
            },
        }

    @staticmethod
    def is_semver_greater(v1, v2):
        v1 = list(map(int, v1.split(".")))
        v2 = list(map(int, v2.split(".")))
        return v1 > v2


class WebSocketHandler:
    def __init__(self, command_processor: CommandProcessor):
        self.command_processor = command_processor
        self.clients = set()

    async def serve(self, host: str, port: int):
        logging.info(f"Starting websocket server on {host}:{port}")
        await websockets.serve(self.ws_handler, host, port)

    async def handle_message(
        self, websocket: websockets.WebSocketServerProtocol, data: Data
    ):
        logging.info(f"Got message: {data}")
        json_data = json.loads(data)
        command, payload = json_data["command"], json_data.get("payload", {})
        try:
            response = await self.command_processor.process_command(command, payload)
            logging.info("Sending response")
        except (
            InvalidSettingException,
            DeviceNotFoundException,
            ValueOutOfRangeException,
            UnknownCommandException,
        ) as e:
            logging.warning(e.message)
            response = {"status": "ERROR", "message": e.message}
        await websocket.send(json.dumps({**response, "command": command}))

    async def ws_handler(self, websocket: websockets.WebSocketServerProtocol):
        try:
            self.clients.add(websocket)
            while True:
                message = await websocket.recv()
                await self.handle_message(websocket, message)
        except websockets.exceptions.ConnectionClosed:
            logging.info("Connection closed")
            self.clients.remove(websocket)

    async def send(self, client: websockets.WebSocketServerProtocol, message: str):
        try:
            await client.send(message)
        except websockets.exceptions.ConnectionClosed:
            pass

    def broadcast(self, message: str):
        for client in self.clients:
            asyncio.create_task(self.send(client, message))
