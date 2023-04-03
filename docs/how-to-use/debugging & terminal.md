# 📒 Debugging & Terminal

## 🧑‍💻 Debug Data

- Debug is a special category in Pinecil that is usually hidden and not used unless troubleshooting an issue.
- On Pinecil, the debug menu is accessed by Long hold [-] and then use the [+] to scroll through the values (see here).
- PineSAM currently displays the raw values as sent by the Pinecil and does no change to the values; therefore, these may not match exactly what you see on the Pinecil Debug screen.
- Not all values are available yet, e.g., PD Debug values can only be seen on Pinecil.

## ⌨️ Terminal Script

- a python script runs the backend server inside a terminal (e.g. powershell)
- Terminal messages contain useful information for devs and troubleshooting.
- BLE MAC address of the pinecil for example is on line "Found pinecil at" `C4:xx:xx:xx:xx:xx`