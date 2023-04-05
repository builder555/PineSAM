# 🚧 Known issues

1. bleak causes Python to crash on Mac: https://github.com/hbldh/bleak/issues/768
    - possible solution: give access to iTerm (or whichever terminal you use) to Bluetooth in Settings
1. Pinecil not detected
    - possible reason: you paired your Pinecil using system settings. solution: unpair it from all other places.  
    - possible reason: using older firmware (below 2.21). solution: [flash](https://github.com/Ralim/IronOS/discussions/1518#discussioncomment-4866637) current [BLE firmware](https://github.com/Ralim/IronOS/suites/11876815030/artifacts/621223733); below IronOS 2.21 only BETA versions will work with PineSAM.
1. main_server script terminal crashes on start of script: incompatible version of IronOS, check/update firmware see above.
1. Windows Powershell issue
    - windows by default does not allow any scripts to run in powershell. Make sure the zip file property is _Unblock_ ([reference](https://github.com/builder555/PineSAM/discussions/106#discussion-4960445)) and set powershell to `RemoteSigned` with:
        ```Powershell
        Set-ExecutionPolicy RemoteSigned
        ```
    - check that windows has not reset the permissions in powershell with
    ```Powershell
    Get-ExecutionPolicy
    ```
    and change it back to `RemoteSigned` if needed ([reference](https://lazyadmin.nl/powershell/running-scripts-is-disabled-on-this-system/)).
1. See the [Discussions](https://github.com/builder555/PineSAM/discussions) section for install hints and solutions to some common issues.
1. PineSAM usage [instructions here](https://github.com/builder555/PineSAM/wiki).
1. Something else: [open an issue](https://github.com/builder555/PineSAM/issues).