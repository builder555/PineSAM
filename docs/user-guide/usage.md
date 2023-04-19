# User Guide

1. Click on PineSAM logo to reveal the unique BLE name of your Pinecil and IronOS build.
2. When a new PineSAM is available, a notice appears under the logo.
3. Current PineSAM version number is next to the Github Cat in the top right.
4. Clicking on the waving cat links to the main Github repository.
5. Temperature automatically adjusts based on °C or °F setting.
6. Colors are designed to work in Light or Dark mode on all browsers.

## :fontawesome-solid-toggle-off: Show Hints

Toggles on/off to display help messages from Pinecil and PineSAM.

## :fontawesome-solid-toggle-off: Save to Flash

- Save changes to flash should be `Off` most of the time. Not needed if actively soldering and using the Work HUD to change temperature (preserves flash cycles).
- Toggle this `On` only before changing settings and if you want the settings to persist on Pinecil reboot. This saves/flashes to the BL706 MCU chip.

## Change Settings

1. Toggle `On` the Save changes to flash.
2. Change multiple settings and when done, toggle it back `Off`.
3. While actively soldering and using buttons in the Work HUD, it is best to leave the save toggle off. No reason to constantly flash to pinecil for each temperature change (don't worry, Pinecil still changes temperature, it's just not permanently flashed and saved on Pinecil).
<div style="clear: both;"></div>

![PineSAM Work View - HUD (Heads Up Display) detailed](../img/workHUD-detailed.png){ align="left" width="400" style="margin-top: -1rem" float="left" }

## Work HUD

1. This is a HUD window designed as an all-in-one single view that can be used during soldering.
2. Phone: designed to be completely viewable on vertical screen.
3. In this view one can control Set temperature with buttons ++plus++ ++minus++ and view important stats, e.g., live temperature.
4. Thermostat icon changes into 100 different color hues as the live temperature changes.
5. Power Bar: bottom bar shows the input voltage, the current estimated watts pinecil is drawing, and the highest peak watt hit during the session.
6. It is best to leave save to flash toggle Off while using the Work HUD to save on pinecil flash cycles as the PineSAM buttons are used often during a soldering session.
<div style="clear: both;"></div>

### Preset buttons

1. Two Preset buttons are available above the power icons. They are exclusive to PineSAM and not available on the Pinecil iron directly.
2. Presets allow quick change of user customized temperatures and can be saved instantly to a desired temperature.
3. Presets are stored in the browser's [LocalStorage](https://developer.mozilla.org/en-US/docs/Web/API/Window/localStorage) and persist if the same browser and device are used again.

### Preset Save

1. Set the number desired with the PineSAM ++plus++ ++minus++ buttons.
2. Then long hold the Preset1 or Preset2 you want to save to, and when a confirmation box opens, click OK.
3. Whatever is in the Set °C at the top of the work HUD will be saved to the Preset button.

## Settings Categories

- For familiarity, Settings are grouped in a similar way as seen on Pinecil (and as organized in Ralim's IronOS firmware).
- Categories can be clicked to collapse and reduce screen clutter.
- Setting numbers can be changed two ways: moving the slider or simply typing on the box next to the slider.
- Drop-down menus are used for clarity of text choices.
- Toggle :fontawesome-solid-toggle-off: choices are used for any check boxes :octicons-checkbox-16: seen on the pinecil (e.g. detailed idle).
- See setting feature details in [Ralim's IronOS here](https://ralim.github.io/IronOS/Settings/).
<br>
![Settings Categories](../img/categories.png)

??? info "Full settings view"
    
    ![Full Settings View](../img/full_settings.png)