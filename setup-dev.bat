@echo off
cd backend
where python3 >nul 2>&1 || (
    echo python3 could not be found
    cd ..
    exit /b
)
python3 -m pip install --user bleak websockets

cd ../ui
where npm >nul 2>&1 || (
    echo npm could not be found
    cd ..
    exit /b
)
rd /s /q node_modules

npm install -D
cd ..
