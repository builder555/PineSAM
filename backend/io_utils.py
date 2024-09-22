import sys
import os
import argparse


def get_resource_path(relative_path: str, max_levels: int = 3):
    """Get the absolute path to the resource, works for development and for PyInstaller"""
    # PyInstaller creates a temp folder and stores path in _MEIPASS
    base_path = getattr(sys, "_MEIPASS", os.path.abspath("."))
    level = 0
    while base_path != "/" and level < max_levels:
        file_path = os.path.join(base_path, relative_path)
        if os.path.exists(file_path):
            break
        base_path = os.path.dirname(base_path)
        level += 1
    else:
        raise FileNotFoundError(f"Could not find resource {relative_path}")
    return os.path.join(base_path, relative_path)


def parse_cmd_args(default_host: str, default_port: int) -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="PineSAM - Pinecil v2 Control")
    parser.add_argument(
        "host",
        nargs="?",
        default=default_host,
        help="Host address (default: %(default)s)",
    )
    parser.add_argument(
        "port",
        nargs="?",
        type=int,
        default=default_port,
        help="Port number (default: %(default)s)",
    )
    parser.add_argument(
        "--no-open", action="store_true", help="Do not open browser page automatically."
    )
    return parser.parse_args()
