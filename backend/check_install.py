from pip._internal import main as pip

try:
    import bleak
except ImportError:
    pip(["install", "bleak"])

try:
    import websockets
except ImportError:
    pip(["install", "websockets"])
