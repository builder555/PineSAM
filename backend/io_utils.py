import sys
import os
import sys
import sys


def resource_path(relative_path):
    """Get the absolute path to the resource, works for development and for PyInstaller"""
    # PyInstaller creates a temp folder and stores path in _MEIPASS
    base_path: str = getattr(sys, "_MEIPASS", os.path.abspath("."))
    return os.path.join(base_path, relative_path)


def parse_cmd_args(default_host, default_port):
    host = sys.argv[1] if len(sys.argv) > 1 else default_host
    port = int(sys.argv[2]) if len(sys.argv) > 2 else default_port

    if len(sys.argv) > 1 and sys.argv[1] in ("-h", "--help"):
        print(f"Usage: {sys.argv[0]} [host] [port]")
        print(f"Example: {sys.argv[0]} 127.0.0.1 8080")
        print(f"Default host: {default_host}")
        print(f"Default port: {default_port}")
        return None, None

    return host, port
