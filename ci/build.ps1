Push-Location ui
npm run build
Pop-Location

pyinstaller --onefile --name Pinecil --hidden-import=winrt.windows.foundation.collections --add-data "./version.txt;./" --add-data "./ui/dist;./gui" backend/main.py
