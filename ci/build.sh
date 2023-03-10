#!/bin/bash

pushd ui || exit 2
npm run build
popd || exit 2

pyinstaller backend/main_server.py
pyinstaller --add-data ui/dist:ui ui/serve.py
