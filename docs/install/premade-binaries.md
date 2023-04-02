## Using pre-made binaries

1. Binary packages do not require installation of python or node.js
2. Download latest [release](https://github.com/builder555/PineSAM/releases/latest) version for your specific OS (Mac, Linux, Windows).
3. **Mac/Linux**: extract and run `./start.sh` in terminal.

   * On MacOS, http://localhost:8080/ opens in your browser automatically.
   * Some Linux distros may need http://localhost:8080/ opened manually.
   * Usage guide [here](https://github.com/builder555/PineSAM/wiki).

4. **Windows**: 
   * right click on the zip, properties> general, check box to Unblock, then extract ([reference](https://github.com/builder555/PineSAM/discussions/106#discussion-4960445)).
   * Run [powershell](https://learn.microsoft.com/en-us/powershell/scripting/install/installing-powershell-on-windows?view=powershell-7.3) as admin, cd to the pinesam folder and `.\start.ps1`
   * Allow any windows pop-up warnings about "serve.exe" and "main_sever.exe".
   * If you get errors in powershell, set the permissions to RemoteSigned to allow scripts ([reference](https://lazyadmin.nl/powershell/running-scripts-is-disabled-on-this-system/)).
     * ```C:\> Set-ExecutionPolicy RemoteSigned```
   * Browser will automatically open http://localhost:8080
   * Usage guide [here](https://github.com/builder555/PineSAM/wiki).
