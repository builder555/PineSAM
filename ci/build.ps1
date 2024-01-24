# Does the build
Push-Location ui
npm run build
Pop-Location

pyinstaller --onefile --add-data "./version.txt;/" --add-data "./ui/dist;/ui" backend/main.py

# pyinstaller backend/main_server.py
# pyinstaller --add-data "ui/dist;ui" ui/serve.py
