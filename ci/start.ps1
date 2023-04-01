$process1 = Start-Process .\main_server\main_server.exe -PassThru

$pid1 = $process1.Id

$process2 = Start-Process .\serve\serve.exe -PassThru

$pid2 = $process2.Id

Write-Output "main_server process ID: $pid1"
Write-Output "server.exe process ID:  $pid2"

Start-Sleep -Seconds 5
Start-Process "http://localhost:8080/"

Get-Process -Id $pid1, $pid2 | Wait-Process
