# 🖥️ Installation Options

## 📦 Using pre-made binaries

1. Binary packages do not require installation of python or node.js
2. Download latest [release](https://github.com/builder555/PineSAM/releases/latest) version for your specific OS (Mac, Linux, Windows).
3. ### Mac/Linux
    - extract and run `./start.sh` in terminal.
    - On MacOS, http://localhost:8080/ opens in your browser automatically.
    - Some Linux distros may need http://localhost:8080/ opened manually.
    - Usage guide [here](https://github.com/builder555/PineSAM/wiki).

4. ### Windows
    - right click on the zip, properties> general, check box to Unblock, then extract ([reference](https://github.com/builder555/PineSAM/discussions/106#discussion-4960445)).
    - Run [powershell](https://learn.microsoft.com/en-us/powershell/scripting/install/installing-powershell-on-windows?view=powershell-7.3) as admin, cd to the pinesam folder and `.\start.ps1`
    - Allow any windows pop-up warnings about "serve.exe" and "main_sever.exe".
    - If you get errors in powershell, set the permissions to RemoteSigned to allow scripts ([reference](https://lazyadmin.nl/powershell/running-scripts-is-disabled-on-this-system/)).
        - ```C:\> Set-ExecutionPolicy RemoteSigned```
    - Browser will automatically open http://localhost:8080
    - Usage guide [here](https://github.com/builder555/PineSAM/wiki).

## 🛠️ Install the Dev version from source

This is the same PineSam as the pre-made binaries. Install this if there is an issue with the binaries or want to contribute / develop on your own.

### Dependencies

- [git](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git)
- [python 3](https://www.python.org/downloads/) (tested with 3.10/3.11)
- [pipenv](https://pipenv.pypa.io/en/latest/installation/)
- [node+npm](https://nodejs.org/en/download/)

### Mac/Linux
  
#### Setup

Install all packages linked above first.

```shell
git clone https://github.com/builder555/PineSAM
cd PineSAM
chmod +x setup-dev.sh
chmod +x run-dev.sh
./setup-dev.sh
```

#### Run

```shell
./run-dev.sh
```
*Press CTRL+C in the terminal window to stop*

- On a Mac http://localhost:8080 will open in your browser automatically.
- Some Linux distros may need http://localhost:8080 opened manually. Debian12 hints [here](https://github.com/builder555/PineSAM/discussions/47#discussion-4884758).

### Windows

#### Install

Install the packages linked above for the backend script. Skip to 4 if you did this already.

1. Python install notes
  -  Check "Add python.exe to PATH" and select "Customize Installation"
  - Check "Add Python to environment variables" option
  - Screenshots of options to select [are here](https://github.com/builder555/PineSAM/discussions/7#discussion-4862766).
1. Install [NodeJS here](https://nodejs.org/en/download), accept all prompts to add packages during install including a prompt in the terminal that opens.
1. After installing packages listed for backend script [reference](https://github.com/builder555/PineSAM/issues/131#issuecomment-1489711241), go to System Environment variables to check paths ([image](https://github.com/builder555/PineSAM/discussions/130#discussion-5011624)).
1. Download the Source-all-_.zip from the [latest release](https://github.com/builder555/PineSAM/releases/latest).
1. If the zip has an Unblock option, then unblock and extract ([example](https://github.com/builder555/PineSAM/discussions/106#discussion-4960445)).
1. Run powershell as administrator, set permissions to RemoteSigned ([image here](https://github.com/builder555/PineSAM/discussions/106)).

```shell
# setting this one time in powershell normally persists on reboots.
C:\Set-ExecutionPolicy RemoteSigned
```

#### Run
- change directory, `cd` into the PineSAM folder that was extracted above.
```shell
.\setup-dev.bat   # only need to run this one time for each new version
.\run-dev.bat     # run this command every time to start PineSAM (do not need to run as admin)
```