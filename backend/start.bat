@echo off
set LOG_LEVEL=info

python check_install.py

start /b python main_server.py
set pidsrv=%ERRORLEVEL%

start /b python -m http.server --directory ../ui 8080
set pidhttp=%ERRORLEVEL% 

ping -n 3 127.0.0.1 > nul
start http://localhost:8080/settings.html

taskkill /f /pid %pidsrv% /pid %pidhttp%
