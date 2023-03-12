Start-Process ./main_server/main_server.exe
$pid1 = $LASTEXITCODE

Start-Process ./serve/serve.exe
$pid2 = $LASTEXITCODE

Start-Sleep -Seconds 5
Start-Process "http://localhost:8080/"

Wait-Process -Id $pid1,$pid2