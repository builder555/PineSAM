# Pinecil V2 settings

Why focus on soldering when you can play with the settings instead? With this app you will have full control over your new shiny Pinecil V2 from your computer.

**NB**: No special browser permissions required

## Features
- [x] Automatically detect Pinecil V2 over BLE
- [x] Get all setting values
- [X] Modify settings
- [ ] Validate setting values before sending to device
- [ ] Adjust temperature ranges based on C/F selection
- [ ] Hide Minimum Voltage (per cell) when source is DC

## Requirements:

- python 3 (tested with 3.10)
- pipenv
- a browser

## Mac/Linux 

### Install

```shell
git clone https://github.com/builder555/pinecil-v2
cd pinecil-v2
pipenv install
chmod +x start.sh
```

### Run
```shell
./start.sh
```

On a Mac http://localhost:8080/settings.html will open in your browser automatically. On linux you need to do it manually (for now).

## Windows

If you already have python installed, you can skip to step 2.

1. Install Python: https://www.python.org/downloads
    * Select "Customize Installation"
    * Check "Add Python to environment variables" option
2. Download this repo: https://github.com/builder555/pinecil-v2/archive/master.zip
3. Unzip it
4. Run start.bat

---

![](./screenshot.png)

## Known issues

- bleak causes Python to crash on Mac: https://github.com/hbldh/bleak/issues/768
    * possible solution: give access to iTerm (or whichever terminal you use) to Bluetooth in Settings
- Pinecil not detected
    * possible solution: need to [flash](https://github.com/Ralim/IronOS/discussions/1518#discussioncomment-4866637) [BLE firmware](https://github.com/Ralim/IronOS/discussions/1449#discussioncomment-4866655)
- Setting change is not reflected on the soldering iron
    * some changes require entering the menu on the device itself (or power cycle after saving to flash) before appearing. [Example](https://github.com/Ralim/IronOS/issues/1560)
- Temperature ranges are out of whack
    * Set your iron temperature to display in Celcius
    
## References

- [Pinecil](https://www.pine64.org/pinecil/) - The Pinecil homepage
- [IronOS](https://github.com/Ralim/IronOS) - The OS running on this soldering iron
- [Pinecil Web UI](https://github.com/joric/pinecil) - A neat web-based UI, requires bluetooth browser support
- [Pinecil Authenticity Checker](https://pinecil.pine64.org/) - Almost all AliExpress Pinecils are fake, check yours!
