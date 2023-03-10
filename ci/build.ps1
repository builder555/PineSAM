# Does the build
Push-Location ui
npm run build
Pop-Location

pyinstaller backend/main_server.py
pyinstaller --add-data "ui/dist;ui" ui/serve.py
