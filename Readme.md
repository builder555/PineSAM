[![Hits](https://hits.seeyoufarm.com/api/count/incr/badge.svg?url=https%3A%2F%2Fgithub.com%2Fbuilder555%2FPineSAM&count_bg=%23FF00BF&title_bg=%23625E5E&icon=pre-commit.svg&icon_color=%23E7E7E7&title=hits&edge_flat=false)](https://github.com/builder555/PineSAM/wiki)
![contributors welcome](https://custom-icon-badges.demolab.com/badge/contributors-welcome-A017A5.svg?logo=star&logoColor=white)
[![Download (all releases)](https://img.shields.io/github/downloads/builder555/pinesam/total?color=A017A5)](https://github.com/builder555/PineSAM/releases/)
[![Latest release](https://img.shields.io/github/v/release/builder555/pinesam?color=7700b3)](https://github.com/builder555/PineSAM/releases/latest)
![bluetooth](https://custom-icon-badges.demolab.com/badge/-bluetooth-7700b3.svg?logo=bluetooth&logoColor=white)
<br><br>
<img src="./images/PineSAM_logo-A017A5.png" align="left" width="150" height="48" style="float:left"> <br clear="left" />
---
<br>
<img src="./images/workHUD.png" align="right" width="350" style="float:left">

#### PineSAM = Pinecil Settings and Menus

Why focus on soldering when you can play with the settings instead? With this app you have full control over your new shiny Pinecil V2 from your computer using bluetooth.

**NB**: No special browser BLE GATT or flags required and works on all major OS/devices.

**NB**: This app needs the python backend to run on a computer, it CANNOT run entirely in the browser like Joric's UI.

<details>
  <summary>
    
#### Full settings view

  </summary>

<img src="./images/full_settings.png" width="900"> 

</details>
<br clear="right"/>

# 💫 Features

- [x] Automatically detect Pinecil V2 over BLE.
- [x] Control all settings on the device.
- [X] Save to Flash: toggle to save changes directly onto Pinecil (leave off unless actively changing settings).
- [X] Work View main screen with: Set °C/°F `[+][-]` buttons, live tip °C/°F updates, peak watts, live watts, input voltage.
- [X] Preset buttons to allow quick change of user defined temperatures (PineSAM extra feature not available directly inside Pinecil).
- [X] Backend runs locally on all major platforms/OS while the user interface runs on your favorite browser.
- [X] See PineSAM Wiki for full [usage details](https://github.com/builder555/PineSAM/wiki/PineSAM
).

## Platforms
 | System  | MacOS | Linux | Windows | iOS | Android|
 | :-----: | :-----: | :---: | :---: | :-: | :----: |
 | UI      |:heavy_check_mark:|:heavy_check_mark:|:heavy_check_mark:|:heavy_check_mark:|:heavy_check_mark:|
 | backend |:heavy_check_mark:|:heavy_check_mark:|:heavy_check_mark:|
<br>

# :desktop_computer: Install Options

## I. Using pre-made binaries

1. Binary packages do not require installation of python or node.js
2. Download latest [release](https://github.com/builder555/PineSAM/releases/latest) version for your specific OS (Mac, Linux, Windows).
3. **Mac/Linux**: extract and run `./start.sh` in terminal.
4. **Windows**: 
   * right click on the zip, properties> general, check box to Unblock, then extract ([reference](https://github.com/builder555/PineSAM/discussions/106#discussion-4960445)).
   * Run powershell as admin, cd to the pinesam folder and `.\start.ps1`
   * Allow any windows pop-up warnings about "serve.exe" and "main_sever.exe".
   * If you get errors in powershell, set the permissions to RemoteSigned to allow scripts ([reference](https://lazyadmin.nl/powershell/running-scripts-is-disabled-on-this-system/)).
   * ```Set-ExecutionPolicy RemoteSigned```

## II. Install the Dev version (Source-all-xxx)

For the backend script, first install:
- [git](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git)
- [python 3](https://www.python.org/downloads/) (tested with 3.10/3.11)
- [pipenv](https://pipenv.pypa.io/en/latest/install/)
- [node+npm](https://nodejs.org/en/download/)
<details>
  <summary>
  
  ### Mac/Linux install
  </summary>
  
#### Setup
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
# press CTRL+C in the terminal window to stop
```
* On a Mac http://localhost:8080 will open in your browser automatically.
* Some Linux distros may need http://localhost:8080 opened manually. Debian12 hints [here](https://github.com/builder555/PineSAM/discussions/47#discussion-4884758).

</details>

<details>
  <summary>
  
### Windows dev install
  </summary>

#### Install
If you already have Python and NodeJS installed, you can skip to step 3.

1. Install Python: https://www.python.org/downloads
    * Check "Add python.exe to PATH" and select "Customize Installation"
    * Check "Add Python to environment variables" option
    * See a reference screen [here](https://github.com/builder555/PineSAM/discussions/7#discussion-4862766).
2. Install NodeJS: https://nodejs.org/en/download/
3. Download the Source-all-xxx from the latest release: https://github.com/builder555/PineSAM/releases/latest
4. Right click the zip and open Properties > General tab and check _Unblock_ if it appears at the bottom. Then Unzip it.
5. Run powershell as administrator, set permissions to RemoteSigned ([reference](https://lazyadmin.nl/powershell/running-scripts-is-disabled-on-this-system/)).
```shell
# setting this one time in powershell normally persists on reboots.
Set-ExecutionPolicy RemoteSigned
```
#### Run
1. Change directory, `cd` to the location of the PineSAM folder that was unzipped above.
```shell
setup-dev.bat   # only need to run this one time for each new version
run-dev.bat     # run this command every time you use Pinecil
```
</details>
<div style="clear:both;">&nbsp;</div>

## :signal_strength: Remote access

You can access the settings remotely once the app is running on the main PC/laptop.

* Find the [local IP address](https://lifehacker.com/how-to-find-your-local-and-external-ip-address-5833108) of the device running the app.
* open `http://<ip-address>:8080/` on the second device on the same network (e.g., a phone).
* Pinecil needs to be within BLE range of the computer running the PineSAM app.

## 🚧 Known issues
1. bleak causes Python to crash on Mac: https://github.com/hbldh/bleak/issues/768
    * possible solution: give access to iTerm (or whichever terminal you use) to Bluetooth in Settings

2. Pinecil not detected
    * possible reason: you paired your Pinecil using system settings. solution: unpair it from all other places.  
    * possible reason: using older firmware (below 2.21). solution: [flash](https://github.com/Ralim/IronOS/discussions/1518#discussioncomment-4866637) [BLE firmware](https://github.com/builder555/PineSAM/files/10797411/Pinecilv2_EN.zip); below IronOS 2.21 only BETA versions will work with PineSAM.

3. Windows Powershell issue
    * windows by default does not allow any scripts to run in powershell. Make sure the zip file property is _Unblock_ ([reference](https://github.com/builder555/PineSAM/discussions/106#discussion-4960445)) and set powershell to remotesigned with:<br/>
    `set-executionpolicy remotesigned`
    * check that windows has not reset the permissions in powershell with `Get-ExecutionPolicy` and change it back to `RemoteSigned` if needed ([reference](https://lazyadmin.nl/powershell/running-scripts-is-disabled-on-this-system/)).
  
4. See the [Discussions](https://github.com/builder555/PineSAM/discussions) section for install hints and solutions to some common issues.
5. PineSAM usage [instructions here](https://github.com/builder555/PineSAM/wiki/PineSAM
).
6. Something else: [open an issue](https://github.com/builder555/PineSAM/issues).


## 🛠️ Running Unit tests

```shell
# run inside 'backend' directory:
pipenv run test
```

## :book: References

- [Pinecil](https://wiki.pine64.org/wiki/Pinecil) - The Pinecil Wiki page
- [IronOS](https://github.com/Ralim/IronOS) - The OS running on this soldering iron
- [Pinecil Web UI](https://github.com/joric/pinecil) - A neat web-based UI, requires bluetooth browser support
- [Pinecil Authenticity Checker](https://pinecil.pine64.org/) - almost all AliExpress Pinecils are fake, check your V2!

