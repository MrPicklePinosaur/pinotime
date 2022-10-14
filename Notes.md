
## terminology

`pynus` - python module to get shell into Nordic's NUS

`gadgetbridge` - android application that can communicate with wasp-os

## Caveats/Issues

GadgetBridge seems to be causing wasp-os to get stuck at the main.py screen if it's trying to connect while the pinetime is booting up

The `wasp/boards/manifest_240x240.py` is very important. If you don't add your module into the list, it will not be built. This is also a nice way of removing files from the build to save memory.
