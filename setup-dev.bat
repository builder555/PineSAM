@echo off
where python3 >nul 2>&1 || (
    echo python3 could not be found
    exit /b
)
where npm >nul 2>&1 || (
    echo npm could not be found
    cd ..
    exit /b
)
cd backend
python3 -m pip install --user bleak websockets

cd ../ui
rd /s /q node_modules
npm install -D
cd ..
