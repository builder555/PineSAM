#!/bin/bash

set -e

pushd ui || exit 2
npm run build
popd || exit 2

pyinstaller --onefile --add-data "./version.txt:/" --add-data "./ui/dist:/gui" backend/main.py --collect-submodules dbus_fast 
