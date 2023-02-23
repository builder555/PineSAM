from pytest import mark
from main_server import main
from main_server import ws_handler
from unittest.mock import AsyncMock, patch
from test_utils import Method


@mark.asyncio
async def test_socket_server_starts_with_main():
    with patch('main_server.websockets.serve') as mock_serve,\
         patch('main_server.asyncio.Future', new=AsyncMock()):
        await main()
        assert Method(mock_serve).was_called_with(ws_handler, '0.0.0.0', 12999)

def test_socket_command_get_settings():
    pass

def test_socket_command_update_setting():
    pass

def test_socket_command_get_info():
    pass
