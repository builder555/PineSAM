@echo off
set LOG_LEVEL=info

cd backend

start /b python main.py
set pidsrv=%ERRORLEVEL%
cd ..\ui

start /b npm run dev
set pidhttp=%ERRORLEVEL% 
cd ..

ping -n 3 127.0.0.1 > nul
start http://localhost:8080

taskkill /f /pid %pidsrv% /pid %pidhttp%
