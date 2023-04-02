# 🖥️ Installation Options

## 📦 Using pre-made binaries

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

## 🛠️ Install the Dev version (Source-all-_.zip)

This is the same PineSam as the pre-made binaries. Install this if there is an issue with the binaries.  
For the backend script, first install:
- [git](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git)
- [python 3](https://www.python.org/downloads/) (tested with 3.10/3.11)
- [pipenv](https://pipenv.pypa.io/en/latest/installation/)
- [node+npm](https://nodejs.org/en/download/)
<details>
  <summary>
  
  Mac/Linux
  </summary>
  
<h4>Setup</h4>
Install all packages linked above first.

```shell
git clone https://github.com/builder555/PineSAM
cd PineSAM
chmod +x setup-dev.sh
chmod +x run-dev.sh
./setup-dev.sh
```

<h4>Run</h4>
```shell
./run-dev.sh
# press CTRL+C in the terminal window to stop
```
<ul>
<li>On a Mac http://localhost:8080 will open in your browser automatically.</li>
<li>Some Linux distros may need http://localhost:8080 opened manually. Debian12 hints <a href="https://github.com/builder555/PineSAM/discussions/47#discussion-4884758">here</a>.</li>
</ul>

</details>

<details>
  <summary>
  
Windows
  </summary>

<h4>Install</h4>
Install the packages linked above for the backend script. Skip to 4 if you did this already.

<ol>
    <li>Python install notes
        <ul>
            <li>* Check "Add python.exe to PATH" and select "Customize Installation"</li>
            <li>* Check "Add Python to environment variables" option</li>
            <li>* Screenshots of options to select <a href="https://github.com/builder555/PineSAM/discussions/7#discussion-4862766">are here</a>.</li>
        </ul>
    </li>
    <li>Install <a href="https://nodejs.org/en/download">NodeJS here</a>, accept all prompts to add packages during install including a prompt in the terminal that opens.</li>
    <li>After installing packages listed for backend script (<a href="https://github.com/builder555/PineSAM/issues/131#issuecomment-1489711241">reference</a>), go to System Environment variables to check paths (<a href="https://github.com/builder555/PineSAM/discussions/130#discussion-5011624">image</a>).</li>
    <li>Download the Source-all-__.zip from the <a href="https://github.com/builder555/PineSAM/releases/latest">latest release</a>.</li>
    <li>If the zip has an Unblock option, then unblock and extract (<a href="https://github.com/builder555/PineSAM/discussions/106#discussion-4960445">example</a>).</li>
    <li>Run powershell as administrator, set permissions to RemoteSigned (<a href="https://github.com/builder555/PineSAM/discussions/106">image here).</li>
</ol>

```shell
# setting this one time in powershell normally persists on reboots.
C:\Set-ExecutionPolicy RemoteSigned
```
<h4>Run</h4>
1. change directory, `cd` into the PineSAM folder that was extracted above.
```shell
.\setup-dev.bat   # only need to run this one time for each new version
.\run-dev.bat     # run this command every time to start PineSAM (do not need to run as admin)
```
</details>