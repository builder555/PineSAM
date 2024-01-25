from pinecil import DeviceNotFoundException
import pytest
from unittest.mock import AsyncMock, MagicMock, patch
from pinecil_monitor import PinecilFinder, PinecilMonitor
import asyncio


class MockPinecil:
    async def connect(self):
        pass

    async def get_live_data(self):
        return {"temp": 100, "voltage": 230}

    @property
    def is_connected(self):
        return True


@pytest.fixture
def pinecils():
    return [MockPinecil(), MockPinecil()]


@pytest.fixture(autouse=True)
def mock_find_pinecils(monkeypatch, pinecils):
    async_mock = AsyncMock(return_value=pinecils)
    monkeypatch.setattr("pinecil_monitor.find_pinecils", async_mock)
    return async_mock


@pytest.mark.asyncio
async def test_find_pinecils(pinecils):
    finder = PinecilFinder()
    await finder.find_pinecils()
    assert len(finder.pinecils) == 2
    assert finder.pinecils == pinecils


@pytest.mark.asyncio
async def test_select_pinecil(pinecils):
    finder = PinecilFinder()
    await finder.find_pinecils()
    finder.select_pinecil(1)
    assert finder.selected == pinecils[1]


@pytest.mark.asyncio
async def test_selecting_pinecil_that_does_not_exist_raises_exception(pinecils):
    finder = PinecilFinder()
    await finder.find_pinecils()
    with pytest.raises(DeviceNotFoundException):
        finder.select_pinecil(3)


@pytest.mark.asyncio
async def test_finder_reset_empties_pinecils_list():
    finder = PinecilFinder()
    await finder.find_pinecils()
    finder.reset()
    assert finder.pinecils == []
    assert finder.selected is None


@pytest.fixture
def mock_pinecil_finder():
    finder = MagicMock(spec=PinecilFinder)
    finder.pinecils = [MockPinecil()]
    finder.selected = None

    def select_pinecil(index):
        finder.selected = finder.pinecils[index]

    finder.select_pinecil = select_pinecil
    return finder


@pytest.fixture
def mock_broadcast():
    return AsyncMock()


@pytest.mark.asyncio
@patch("asyncio.sleep", new_callable=AsyncMock)
async def test_monitor_no_pinecil_found(
    mock_sleep, mock_pinecil_finder, mock_broadcast
):
    stop_event = asyncio.Event()
    monitor = PinecilMonitor(mock_pinecil_finder, mock_broadcast)
    mock_pinecil_finder.pinecils = []
    asyncio.create_task(monitor.monitor(stop_event))
    await asyncio.sleep(0.1)
    stop_event.set()
    assert not mock_broadcast.called


@pytest.mark.asyncio
async def test_monitor_success(mock_pinecil_finder, mock_broadcast):
    stop_event = asyncio.Event()
    mock_broadcast_sets_event = AsyncMock(side_effect=lambda msg: stop_event.set())

    monitor = PinecilMonitor(mock_pinecil_finder, mock_broadcast_sets_event)
    asyncio.create_task(monitor.monitor(stop_event))
    await asyncio.sleep(0.2)
    mock_broadcast_sets_event.assert_called_with(
        '{"command": "LIVE_DATA", "payload": {"temp": 100, "voltage": 230}, "status": "OK"}'
    )


# Add more tests for different scenarios (pinecil not connected, device disconnected exception, etc.)
