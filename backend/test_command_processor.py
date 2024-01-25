import pytest
from unittest.mock import AsyncMock, MagicMock
from ws_server import (
    Pinecil,
    PinecilFinder,
    CommandProcessor,
    VersionChecker,
    DeviceDisconnectedException,
    DeviceNotFoundException,
    UnknownCommandException,
)


@pytest.fixture
def mock_finder():
    mock = MagicMock(spec=PinecilFinder)
    mock.selected = AsyncMock(spec=Pinecil)
    return mock


@pytest.fixture
def mock_app_version_manager():
    mock = MagicMock(spec=VersionChecker)
    mock.read_version.return_value = "1.0.0"
    mock.get_latest_version.return_value = "1.1.0"
    return mock


@pytest.fixture
def mock_ironos_version_manager():
    mock = MagicMock(spec=VersionChecker)
    mock.get_latest_version.return_value = "1.1.0"
    return mock


@pytest.fixture
def command_processor(
    mock_finder, mock_app_version_manager, mock_ironos_version_manager
):
    return CommandProcessor(
        mock_finder, mock_app_version_manager, mock_ironos_version_manager
    )


@pytest.mark.asyncio
async def test_process_command_get_app_info(command_processor):
    response = await command_processor.process_command("GET_APP_INFO", {})
    assert response == {
        "status": "OK",
        "payload": {"app_version": "1.0.0", "is_new_available": True},
    }


@pytest.mark.asyncio
async def test_process_command_get_settings(command_processor, mock_finder):
    mock_finder.selected.get_all_settings = AsyncMock(
        return_value={"setting1": "value1"}
    )
    response = await command_processor.process_command("GET_SETTINGS", {})
    assert response == {"status": "OK", "payload": {"setting1": "value1"}}


@pytest.mark.asyncio
async def test_update_setting_command_sets_pinecil_settings(
    command_processor, mock_finder
):
    mock_finder.selected.set_one_setting = AsyncMock()
    mock_finder.selected.save_to_flash = AsyncMock()
    response = await command_processor.process_command(
        "UPDATE_SETTING", {"name": "setting1", "value": "value2", "save": True}
    )
    mock_finder.selected.set_one_setting.assert_called_once_with("setting1", "value2")
    mock_finder.selected.save_to_flash.assert_called_once()
    assert response == {"status": "OK"}


@pytest.mark.asyncio
async def test_get_info_command_returns_proper_data(
    command_processor, mock_finder, mock_ironos_version_manager
):
    mock_finder.selected.get_info = AsyncMock(return_value={"build": "1.0.0"})
    response = await command_processor.process_command("GET_INFO", {})
    assert response == {
        "status": "OK",
        "payload": {
            "build": "1.0.0",
            "latest_build": "1.1.0",
            "is_new_build_available": True,
        },
    }


@pytest.mark.asyncio
async def test_unknown_command_raises_exception(command_processor):
    with pytest.raises(UnknownCommandException):
        await command_processor.process_command("SOME_RANDOM_COMMAND", {})


@pytest.mark.asyncio
async def test_pinecil_not_selected_raises_device_not_found_exception_when_processing_commands(
    command_processor, mock_finder
):
    mock_finder.selected = None
    with pytest.raises(DeviceNotFoundException):
        await command_processor.process_command("GET_SETTINGS", {})


@pytest.mark.asyncio
async def test_pinecil_disconnected_raises_exception_when_processing_commands(
    command_processor, mock_finder
):
    mock_finder.selected.is_connected = False
    with pytest.raises(DeviceDisconnectedException):
        await command_processor.process_command("GET_SETTINGS", {})
