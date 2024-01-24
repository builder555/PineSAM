Push-Location ui
npm run build
Pop-Location

pyinstaller --onefile --add-data "./version.txt;/" --add-data "./ui/dist;/gui" backend/main.py
