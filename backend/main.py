import asyncio
import os
from pinecil_monitor import PinecilMonitor, PinecilFinder
from ws_server import CommandProcessor, WebSocketHandler
from version_checker import VersionChecker
import logging

LOG_LEVEL = os.environ.get("LOG_LEVEL", "INFO").upper()
timestamp_format = "%H:%M:%S"
logging.basicConfig(
    level=LOG_LEVEL,
    format="%(asctime)s.%(msecs)03d::%(levelname)s::%(message)s",
    datefmt=timestamp_format,
)


async def main(stop_event=asyncio.Event()):
    parent_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    pinesam_url = "https://api.github.com/repos/builder555/PineSAM/releases/latest"
    ironos_url = "https://api.github.com/repos/Ralim/IronOS/releases/latest"
    version_file = os.path.join(parent_dir, "version.txt")
    print(version_file)
    app_version_manager = VersionChecker(file_path=version_file, api_url=pinesam_url)
    ironos_version_manager = VersionChecker(api_url=ironos_url)

    pinecil_finder = PinecilFinder()
    command_processor = CommandProcessor(
        pinecil_finder, app_version_manager, ironos_version_manager
    )
    ws_handler = WebSocketHandler(command_processor)
    pinecil_monitor = PinecilMonitor(pinecil_finder, ws_handler.broadcast)

    tasks = [
        asyncio.create_task(ws_handler.serve("0.0.0.0", 12999)),
        asyncio.create_task(pinecil_monitor.monitor(stop_event)),
    ]
    await asyncio.gather(*tasks)


if __name__ == "__main__":
    asyncio.run(main())
