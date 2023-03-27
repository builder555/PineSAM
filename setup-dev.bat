@echo off
where python >nul 2>&1 || (
    echo python could not be found
    exit /b
)
where npm >nul 2>&1 || (
    echo npm could not be found
    cd ..
    exit /b
)
cd backend
python -m pip install --user bleak websockets requests

cd ../ui
rd /s /q node_modules
npm install -D
cd ..
