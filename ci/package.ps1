$name = $args[0]

if ([string]::IsNullOrWhiteSpace($name)) {
Write-Host "usage: ./package.ps1 Package-Name"
exit 1
}

$zip_path = "$(Get-Location)/$name.zip"

Push-Location dist
Compress-Archive -Path PineSAM.exe  -DestinationPath $zip_path -Force
Pop-Location

Write-Output "asset_path=$zip_path" >> $Env:GITHUB_OUTPUT
Write-Output "asset_name=${name}.zip" >> $Env:GITHUB_OUTPUT