from pinecil import DeviceNotFoundException
import pytest
from unittest.mock import AsyncMock
from pinecil_monitor import PinecilFinder

# Mock Pinecil object if necessary
class MockPinecil:
    pass

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
