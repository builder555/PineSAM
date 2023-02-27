import asyncio
import pytest
import json
from ble import DeviceDisconnectedException
from main_server import main
from main_server import ws_handler
from main_server import pinecil_monitor
from unittest.mock import AsyncMock, patch, MagicMock
from test_utils import Method

mock_clients = [1,2,3]

async def complete_task(a_task, stop_event):
    with pytest.raises(asyncio.TimeoutError):
        await asyncio.wait_for(a_task, 0.1)
    stop_event.set()

@pytest.fixture
def patched_main():
    with (patch('main_server.pinecil_monitor', new=AsyncMock()) as mock_monitor,
            patch('main_server.websockets.serve', new=AsyncMock()) as mock_ws_serve):
        yield main, mock_monitor, mock_ws_serve

@pytest.mark.asyncio
async def test_websocket_listens_on_correct_host_and_port(patched_main):
    main, _, mock_ws_serve = patched_main
    await main()
    assert Method(mock_ws_serve).was_called_with(ws_handler, '0.0.0.0', 12999)

@pytest.mark.asyncio
async def test_pinecil_monitor_runs(patched_main):
    main, mock_pinecil_monitor, _ = patched_main
    await main()
    assert mock_pinecil_monitor.called

@pytest.mark.asyncio
@patch('main_server.CLIENTS', mock_clients)
@patch('main_server.send')
async def test_pinecil_monitor_broadcasts_data_from_pinecil_to_clients(mock_ws_send):
    mock_live_data = {
        'LiveTemp': 28,
        'Voltage': 51,
        'HandleTemp': 282,
        'OperatingMode': 1,
        'Watts': 24,
    }
    expected_command = json.dumps({'command': 'LIVE_DATA', 'payload': mock_live_data})
    fake_pinecil = MagicMock(get_live_data=AsyncMock(return_value=mock_live_data), is_connected=True)
    with patch('main_server.pinecil', fake_pinecil):
        stop_event = asyncio.Event()
        monitor_task = asyncio.create_task(pinecil_monitor(stop_event))
        await complete_task(monitor_task, stop_event)

        assert mock_ws_send.call_count > 0 and mock_ws_send.call_count == len(mock_clients)
        for client in mock_clients:
            assert Method(mock_ws_send).was_called_with(client, expected_command)

@pytest.mark.asyncio
@patch('main_server.CLIENTS', mock_clients)
@patch('main_server.send', AsyncMock())
async def test_pinecil_monitor_reads_data_only_once_per_cycle():
    fake_pinecil = MagicMock(get_live_data=AsyncMock(return_value={}), is_connected=True)
    with patch('main_server.pinecil', fake_pinecil):
        stop_event = asyncio.Event()
        monitor_task = asyncio.create_task(pinecil_monitor(stop_event))
        await complete_task(monitor_task, stop_event)
        assert len(mock_clients) > 1
        assert fake_pinecil.get_live_data.call_count == 1

@pytest.mark.asyncio
@patch('main_server.CLIENTS', mock_clients)
@patch('main_server.send')
async def test_pinecil_monitor_announces_device_disconnect(mock_ws_send):
    async def simulate_disconnect():
        fake_pinecil.is_connected = False
        raise DeviceDisconnectedException
    fake_pinecil = MagicMock(
        get_live_data=AsyncMock(side_effect=simulate_disconnect),
        is_connected=True,
    )
    with patch('main_server.pinecil', fake_pinecil):
        stop_event = asyncio.Event()
        monitor_task = asyncio.create_task(pinecil_monitor(stop_event))
        await complete_task(monitor_task, stop_event)
        expected_msg = json.dumps({'status': 'ERROR', 'message': 'Device disconnected'})
        assert Method(mock_ws_send).was_called_with(1, expected_msg)

def test_socket_command_get_settings():
    pass

def test_socket_command_update_setting():
    pass

def test_socket_command_get_info():
    pass
