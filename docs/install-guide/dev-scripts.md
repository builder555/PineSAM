# Build dev version from scripts

Use this development (dev) version if there is an issue with the premade binaries or you want to do PineSAM dev.

In the end, this version produces the same PineSAM as the premade binaries from the [Easy Install](easy-install.md).

## :material-clipboard-check-outline: Dependencies

- [git](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git)
- [python 3](https://www.python.org/downloads/) (tested with 3.10/3.11)
- [pipenv](https://pipenv.pypa.io/en/latest/installation/)
- [node+npm](https://nodejs.org/en/download/)


## :fontawesome-brands-apple: Mac or :fontawesome-brands-linux: Linux dev

#### Setup
First, install all packages linked above in [dependencies](#dependencies).

```shell title="then get pinesam"
git clone https://github.com/builder555/PineSAM
cd PineSAM
chmod +x setup-dev.sh
chmod +x run-dev.sh
./setup-dev.sh
```

#### Run
```shell
./run-dev.sh
# press CTRL+C in the terminal window to stop
```

* On a Mac, PineSAM will automatically open http://localhost:8080 will open in your default browser.
* Some Linux distros may need http://localhost:8080 opened manually. Debian12 hints [here](https://github.com/builder555/PineSAM/discussions/47#discussion-4884758).
* To run from a phone [see :material-cellphone-nfc:](../index.md#remote-access)
* See [Troubleshooting](troubleshooting.md) for more help.
<br>
  
## :fontawesome-brands-windows: Windows dev

#### Setup

Follow the additional hints below to install all packages linked above in [dependencies](#dependencies).

1. Python install notes
    * Check "Add python.exe to PATH" and select "Customize Installation"
    * Check "Add Python to environment variables" option
    * Screenshots of options to select [are here](https://github.com/builder555/PineSAM/discussions/7#discussion-4862766).
2. Install [NodeJS here](https://nodejs.org/en/download/), accept all prompts to add packages during install including a prompt in the terminal that opens.
3. After installing packages listed for backend script ([reference](https://github.com/builder555/PineSAM/issues/131#issuecomment-1489711241)), go to System Environment variables to check paths ([image](https://github.com/builder555/PineSAM/discussions/130#discussion-5011624)).
4. Download the Source-all-__.zip from the latest [releases](https://github.com/builder555/PineSAM/releases/latest).
5. Right-click the zip > properties, if it has an Unblock option, then unblock and extract it ([example](https://github.com/builder555/PineSAM/discussions/106#discussion-4960445)).
6. Run powershell as administrator, set permissions to `RemoteSigned` ([reference](https://github.com/builder555/PineSAM/discussions/106)). Setting this one time in powershell is usually enough as it persists on reboot.
```console
C:\> Set-ExecutionPolicy RemoteSigned
```
7. Then check that powershell permissions are correct; at minimum, need LocalMachine to show as `RemoteSigned` (Unrestricted also works).
```console
C:\> Get-executionPolicy -List
```

#### Run

Change directory (`cd`) into the PineSAM folder that was extracted above.
```shell
.\setup-dev.bat   # only need to run this one time for each new version
.\run-dev.bat     # run this command every time to start PineSAM (do not need to run as admin)
```

* To run from a phone [see :material-cellphone-nfc:](../index.md#remote-access)
* See [Troubleshooting](troubleshooting.md) for more help.