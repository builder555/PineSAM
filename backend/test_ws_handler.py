import json
import pytest
import websockets
import asyncio
from unittest.mock import AsyncMock, MagicMock, patch
from ws_server import WebSocketHandler, UnknownCommandException, CommandProcessor


@pytest.fixture
def mock_command_processor():
    processor = MagicMock(spec=CommandProcessor)
    processor.process_command = AsyncMock()
    return processor


@pytest.fixture
def mock_websocket():
    ws = MagicMock(spec=websockets.WebSocketServerProtocol)
    ws.send = AsyncMock()
    ws.recv = AsyncMock()
    ws.close = AsyncMock()
    return ws


@pytest.fixture
def websocket_handler(mock_command_processor):
    return WebSocketHandler(mock_command_processor, "/ui/path")


@pytest.mark.asyncio
async def test_broadcast_sends_message_to_all_clients(
    websocket_handler, mock_websocket
):
    clients = {AsyncMock(), AsyncMock()}
    websocket_handler.clients = clients

    msg = "test message"
    await websocket_handler.broadcast(msg)

    for client in clients:
        client.send.assert_called_once_with(msg)


@pytest.mark.asyncio
@patch("ws_server.websockets.serve", new_callable=AsyncMock)
async def test_serve_calls_websocket_with_specified_host_and_port(
    mock_websocket_serve, websocket_handler
):
    host = "localhost"
    port = 1234

    await websocket_handler.serve(host, port)

    mock_websocket_serve.assert_called_once()
    args, kwargs = mock_websocket_serve.call_args

    assert host == kwargs.get("host") or host == args[1]
    assert port == kwargs.get("port") or port == args[2]


def run_once(exception):
    def decorator(f):
        async def wrapper(*args, **kwargs):
            if not wrapper.has_run:
                wrapper.has_run = True
                return await f(*args, **kwargs)
            raise exception

        wrapper.has_run = False
        return wrapper

    return decorator


@pytest.mark.asyncio
async def test_handle_message_and_send_response(
    websocket_handler, mock_command_processor
):
    mocker = AsyncMock()

    async def grab_ws_handler(
        ws_handler, host, port, create_protocol=lambda *a, **kw: None
    ):
        mocker.simulate_ws_message = ws_handler
        return AsyncMock()

    @run_once(exception=websockets.exceptions.ConnectionClosed(None, None))
    async def send_response_once(command, payload):
        return {"status": "OK", "message": "Success", "payload": "some info"}

    mock_command_processor.process_command = send_response_once
    fake_incoming_ws_message = json.dumps({"command": "GET_INFO"})
    fake_ws_client = AsyncMock()
    fake_ws_client.recv.return_value = fake_incoming_ws_message

    with patch("ws_server.websockets.serve", new=grab_ws_handler):
        await websocket_handler.serve("localhost", 1234)
        await mocker.simulate_ws_message(fake_ws_client)
        fake_ws_client.send.assert_called_once_with(
            json.dumps(
                {
                    "status": "OK",
                    "message": "Success",
                    "payload": "some info",
                    "command": "GET_INFO",
                }
            )
        )
