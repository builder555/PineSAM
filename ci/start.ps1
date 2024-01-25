$process1 = Start-Process .\Pinecil.exe -PassThru

$pid1 = $process1.Id

Write-Output "Pinecil process ID: $pid1"

Start-Sleep -Seconds 5
Start-Process "http://localhost:8080/"

Get-Process -Id $pid1 | Wait-Process
