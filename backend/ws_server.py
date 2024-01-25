import asyncio
import logging
import json
import http
import os
import mimetypes
import websockets
from websockets import WebSocketServerProtocol
import websockets.exceptions
from websockets.typing import Data
from pinecil import DeviceNotFoundException
from pinecil import InvalidSettingException
from pinecil import ValueOutOfRangeException
from pinecil import DeviceDisconnectedException
from pinecil import Pinecil
from pinecil_monitor import PinecilFinder
from version_checker import VersionChecker, is_semver_greater


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
    def _pinecil(self) -> Pinecil:
        if not self.finder.selected:
            raise DeviceNotFoundException()
        if not self.finder.selected.is_connected:
            raise DeviceDisconnectedException()
        return self.finder.selected

    async def process_command(self, command: str, payload: dict) -> dict:
        if command == "GET_APP_INFO":
            return await self._get_app_info()
        elif command == "GET_SETTINGS":
            return await self._get_settings()
        elif command == "UPDATE_SETTING":
            return await self._update_setting(payload)
        elif command == "GET_INFO":
            return await self._get_info()
        else:
            raise UnknownCommandException()

    async def _get_app_info(self) -> dict:
        app_current_version = self.app_ver.read_version()
        app_latest_version = self.app_ver.get_latest_version()
        return {
            "status": "OK",
            "payload": {
                "app_version": app_current_version,
                "is_new_available": is_semver_greater(
                    app_latest_version, app_current_version
                ),
            },
        }

    async def _get_settings(self) -> dict:
        settings = await self._pinecil.get_all_settings()
        return {"status": "OK", "payload": settings}

    async def _update_setting(self, payload):
        await self._pinecil.set_one_setting(payload["name"], payload["value"])
        if payload.get("save"):
            await self._pinecil.save_to_flash()
        return {"status": "OK"}

    async def _get_info(self) -> dict:
        info = await self._pinecil.get_info()
        latest_build = self.ironos_ver.get_latest_version()
        return {
            "status": "OK",
            "payload": {
                **info,
                "latest_build": latest_build,
                "is_new_build_available": is_semver_greater(
                    latest_build, info["build"]
                ),
            },
        }


def make_protocol(ui_path: str):
    class HTTPServerProtocol(WebSocketServerProtocol):
        async def process_request(self, path, request_headers):
            is_ws_request = "Upgrade" in request_headers
            if not is_ws_request:
                return self._handle_http_request(path)

        def _get_content_type(self, filepath):
            """
            Returns the MIME type based on the file extension.
            """
            content_type, _ = mimetypes.guess_type(filepath)
            return content_type or "application/octet-stream"

        def _handle_http_request(self, path):
            if not ui_path:
                return http.HTTPStatus.NOT_FOUND, [], b"404 Not Found"
            if path == "/" or path == "":
                path = "/index.html"
            filepath = os.path.join(ui_path, path.lstrip("/"))
            if os.path.exists(filepath) and os.path.isfile(filepath):
                content_type = self._get_content_type(filepath)
                with open(filepath, "rb") as f:
                    content = f.read()
                response_headers = [
                    ("Content-Type", content_type),
                    ("Content-Length", str(len(content))),
                ]
                return http.HTTPStatus.OK, response_headers, content
            else:
                return http.HTTPStatus.NOT_FOUND, [], b"404 Not Found"

    return HTTPServerProtocol


class WebSocketHandler:
    def __init__(self, command_processor: CommandProcessor, ui_path: str):
        self.command_processor = command_processor
        self.clients = set()
        self._ui_path = ui_path

    async def serve(self, host: str, port: int):
        logging.info(f"Starting websocket server on {host}:{port}")
        await websockets.serve(
            self._ws_handler, host, port, create_protocol=make_protocol(self._ui_path)
        )

    def broadcast(self, message: str):
        for client in self.clients:
            asyncio.create_task(self._send(client, message))

    async def _handle_message(
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

    async def _ws_handler(self, websocket: websockets.WebSocketServerProtocol):
        try:
            self.clients.add(websocket)
            while True:
                message = await websocket.recv()
                await self._handle_message(websocket, message)
        except websockets.exceptions.ConnectionClosed:
            logging.info("Connection closed")
            self.clients.remove(websocket)

    async def _send(self, client: websockets.WebSocketServerProtocol, message: str):
        try:
            await client.send(message)
        except websockets.exceptions.ConnectionClosed:
            pass
