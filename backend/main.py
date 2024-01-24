import asyncio
import os
from pinecil_monitor import PinecilMonitor, PinecilFinder
from ws_server import CommandProcessor, WebSocketHandler
from version_checker import VersionChecker
import logging
from io_utils import parse_cmd_args, resource_path

LOG_LEVEL = os.environ.get("LOG_LEVEL", "INFO").upper()
timestamp_format = "%H:%M:%S"
logging.basicConfig(
    level=LOG_LEVEL,
    format="%(asctime)s.%(msecs)03d::%(levelname)s::%(message)s",
    datefmt=timestamp_format,
)

DEFAULT_HOST = "0.0.0.0"
DEFAULT_PORT = 8080

async def main(stop_event=asyncio.Event()):
    host, port = parse_cmd_args(DEFAULT_HOST, DEFAULT_PORT)
    if not host or not port:
        return

    pinesam_url = "https://api.github.com/repos/builder555/PineSAM/releases/latest"
    ironos_url = "https://api.github.com/repos/Ralim/IronOS/releases/latest"
    app_version_manager = VersionChecker(api_url=pinesam_url, file_path=resource_path('version.txt'))
    ironos_version_manager = VersionChecker(api_url=ironos_url)

    pinecil_finder = PinecilFinder()
    command_processor = CommandProcessor(
        pinecil_finder, app_version_manager, ironos_version_manager
    )
    ws_handler = WebSocketHandler(command_processor, ui_path=resource_path('gui'))
    pinecil_monitor = PinecilMonitor(pinecil_finder, ws_handler.broadcast)
    tasks = [
        asyncio.create_task(ws_handler.serve(host, port)),
        asyncio.create_task(pinecil_monitor.monitor(stop_event)),
    ]
    await asyncio.gather(*tasks)


if __name__ == "__main__":
    asyncio.run(main())
