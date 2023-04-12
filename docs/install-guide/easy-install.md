
# Easy Install

Easiest way to install PineSAM is using a premade binary package; does not require installation of python, node.js, or other dependencies.

Just download the latest [release](https://github.com/builder555/PineSAM/releases/latest) for a specific OS name and follow the steps below.

## :fontawesome-brands-apple: Mac or :fontawesome-brands-linux: Linux

* Extract the downloaded zip file for Mac or Linux from [here](https://github.com/builder555/PineSAM/releases/latest).
   
   
``` sh title="Run in a terminal"
./start.sh
```
   
* On MacOS, http://localhost:8080/ opens in your browser automatically.
* Some Linux distros may need http://localhost:8080/ opened manually.
* To run from a phone [see :material-cellphone-nfc:](../index.md#remote-access)
* User [guide here](../user-guide/usage.md).
* See [Troubleshooting](troubleshooting.md) for help.

## :fontawesome-brands-windows: Windows

* Download the zip for Windows from [here](https://github.com/builder555/PineSAM/releases/latest).
* Right-click the zip > properties, if it has an Unblock option, then unblock and extract the zip ([reference](https://github.com/builder555/PineSAM/discussions/106#discussion-4960445)).
* Inside powershell, change to the directory where the files were extracted.

``` console title="Run powershell, path may differ from example"
C:\> cd .\Downloads\PineSAM\
C:\> .\start.ps1
```

* Accept any pop-up warnings about "serve.exe" and "main_sever.exe" ([reference](https://github.com/builder555/PineSAM/discussions/106#discussion-4960445)).

* Your default browser will automatically open http://localhost:8080
* To run from a phone [see :material-cellphone-nfc:](../index.md#remote-access)
* User [guide here](../user-guide/usage.md).
<br>

* If there are errors, run [Powershell](https://learn.microsoft.com/en-us/powershell/scripting/install/installing-powershell-on-windows?view=powershell-7.3) as administrator.

* Then use this command to set permissions to `RemoteSigned` to allow pwsh to execute scripts ([reference](https://lazyadmin.nl/powershell/running-scripts-is-disabled-on-this-system/)). 

``` console
C:\> Set-ExecutionPolicy RemoteSigned
```

* See [Troubleshooting](troubleshooting.md) for help.