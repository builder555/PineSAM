import asyncio
import logging
import json
from pinecil import Pinecil, find_pinecils
from pinecil import DeviceDisconnectedException
from pinecil import DeviceNotFoundException
from typing import Callable


class PinecilFinder:
    def __init__(self):
        self.pinecils = []
        self.selected: Pinecil | None = None

    def select_pinecil(self, index: int):
        if not 0 <= index < len(self.pinecils):
            raise DeviceNotFoundException()
        self.selected = self.pinecils[index]

    async def find_pinecils(self):
        logging.info("looking for pinecil...")
        self.pinecils = await find_pinecils()

    def reset(self):
        self.pinecils = []
        self.selected = None


class PinecilMonitor:
    def __init__(self, finder: PinecilFinder, broadcast_func: Callable):
        self.pinecil_finder = finder
        self.broadcast = broadcast_func
        self.should_announce_not_found = True

    @property
    def pinecil(self) -> Pinecil | None:
        return self.pinecil_finder.selected

    async def monitor(self, stop_event: asyncio.Event):
        logging.info("Starting pinecil monitor")
        while not stop_event.is_set():
            if not self.pinecil_finder.pinecils:
                logging.info("looking for pinecil...")
                await self.pinecil_finder.find_pinecils()
                continue
            if not self.pinecil:
                self.pinecil_finder.select_pinecil(0)
                continue
            if not self.pinecil.is_connected:
                logging.info("Connecting to pinecil...")
                try:
                    await self.pinecil.connect()
                    logging.info("Pinecil connected")
                except DeviceNotFoundException as e:
                    logging.warning(e.message)
                    response = {"status": "ERROR", "message": e.message}
                    if self.should_announce_not_found:
                        await self.broadcast(json.dumps(response))
                    self.should_announce_not_found = False
                    self.pinecil_finder.reset()
                await asyncio.sleep(1)
                continue
            try:
                self.should_announce_not_found = True
                pinecil_data = await self.pinecil.get_live_data()
                msg = json.dumps(
                    {"command": "LIVE_DATA", "payload": pinecil_data, "status": "OK"}
                )
                await self.broadcast(msg)
            except DeviceDisconnectedException:
                logging.info("Pinecil disconnected")
                await self.broadcast(
                    json.dumps({"status": "ERROR", "message": "Device disconnected"})
                )
            except Exception as e:
                logging.warning("Error while getting live data - ignored")
