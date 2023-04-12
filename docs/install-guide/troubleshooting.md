
## :material-information-slab-box-outline: Known issues

1. Pinecil not detected
    * possible reason: pinecil is paired to computer/phone settings. solution: unpair it from all other places and reboot.
    * possible reason: using older firmware (below 2.21). solution: [flash](https://github.com/Ralim/IronOS/discussions/1518#discussioncomment-4866637) current [BLE firmware](https://github.com/Ralim/IronOS/releases); below IronOS 2.21 only BETA versions will work with PineSAM.

2. bleak causes Python to crash on Mac: https://github.com/hbldh/bleak/issues/768
    * possible solution: give access to iTerm (or whichever terminal you use) to Bluetooth in Settings

3. main_server script terminal crashes on start of script: incompatible version of IronOS, check/update firmware see above.

4. Windows Powershell issue
    * windows by default does not allow any scripts to run in powershell. Make sure the zip file property is _Unblock_ ([reference](https://github.com/builder555/PineSAM/discussions/106#discussion-4960445)) and set powershell to remotesigned with:<br/>
    `set-executionpolicy remotesigned`
    * check that windows has not reset the permissions in powershell with `Get-ExecutionPolicy` and change it back to `RemoteSigned` if needed ([reference](https://lazyadmin.nl/powershell/running-scripts-is-disabled-on-this-system/)).
  
5. See the [Discussions](https://github.com/builder555/PineSAM/discussions) section for install hints, screenshot images, and solutions to common issues.

6. Something else: [open an issue :octicons-issue-opened-16:](https://github.com/builder555/PineSAM/issues).

## :octicons-terminal-24: Running Unit tests 
```shell title="Run inside 'backend' folder"
pipenv run test
```