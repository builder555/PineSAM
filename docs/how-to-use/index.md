# 🗃️ How to use

## 🔖 Usage

1. PineSAM user interface runs in any browser.
   1. On Windows/MacOS, http://localhost:8080/  opens in your browser automatically.   
   1. Some Linux distros may need http://localhost:8080/ opened manually.
1. The backend is a python script that runs in a terminal window that could be minimized or used for debugging.
1. Click on PineSAM logo to reveal the unique BLE name of your Pinecil.
1. Update available notice appears under the PineSAM logo if a new release is available for download.
1. PineSAM version number is next to the Github Cat in the top right of the screen.
1. Clicking on the waving cat links to the main Github PineSAM repo.
1. Show Hints: toggles on/off to display help messages from Pinecil and PineSAM.
1. Temperature automatically adjusts based on °C or °F setting.
1. Colors are designed to work in Light or Dark view mode on PC and Phone Browsers.
1. Thermostat icon changes into 100 different color hues as the live temperature changes.

### 💾 Save Changes to Flash

- In Work HUD view, leave Save to Flash OFF (not needed and preserves flash cycles).
- Toggle this on ''only'' before changing settings on the Pinecil so they persist on reboot.

**Steps to Change Settings:**

1. toggle on the Save to Flash (grey is off)
1. change all desired settings
1. once complete, toggle it off.
1. if using the Work HUD view, it is best to leave this off. No reason to constantly flash to pinecil for each temperature change (don't worry Pinecil still changes temperature, it's just not permanently flashed and set).

---

## 🧑‍🏭 Work HUD View

<img src="../assets/img/workHUD-detailed.png" width="475px" align="right">

1. This is a HUD window designed as an all-in-one single view that can be used during soldering.
1. Phone: designed to be completely viewable on vertical screen.
1. In this view one can control Set temperature with buttons +/- and view important stats, e.g., live temperature.
1. Power Bar: bottom bar shows the input voltage, the current estimated watts pinecil is drawing, and the highest peak watt hit during the session.
1. It is best to leave save to flash toggle Off while using the Work HUD to save on pinecil flash cycles as the PineSAM buttons are used often during a soldering session.

### 🎛️ Preset buttons

1. Allows quick change of user customizable temperatures (exclusive to PineSAM and not available on Pinecil iron directly).
1. Preset buttons can be customized and saved instantly to desired temperature.
1. Presets are saved to the html file where the python script is running and will persist if one uses the same PC again.

**Steps:**

1. set the number desired with the PineSAM [-][+] buttons.
1. then long hold the Preset 1/2 you want to save to, click OK on the confirmation box.
1. it will save what is currently shown in the Set °C at the top.
