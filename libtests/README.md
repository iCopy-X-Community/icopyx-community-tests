# X11 and keys

Binding HMI keys to X11:
```
sudo apt install libxdo3 xdotool libxdo-dev
sudo python3 -m pip install python-libxdo
```

# readbat

Simple communication with STM32 to retrieve battery percentage.
```
./readbat.sh
```

# test_screen

Simple example to drive the screen and receive STM32 key events.

```
./test_screen.sh
```
It can also run on the host with the following key bindings defined in `keymap.py`:

|M1|M2|UP|DOWN|LEFT|RIGHT|OK|POWER|ALL|
|-|-|-|-|-|-|-|-|-|
|,|.|Up|Down|Left|Right|Enter|R_Alt|R_Ctrl

# turtledemo

Simple example to drive the screen and receive STM32 key events.

```
./turtledemo.sh
```
Buttons:
* UP to move forward
* LEFT to turn left by 22.5 degrees
* RIGHT to turn right by 22.5 degrees
* M1 to clear the drawing
* M2 to toggle the pen up/down
* POWER to reset entirely the drawing and pen

It can also run on the host with the same key bindings as `test_screen.sh`.

# xbubble

Example to control a game with STM32 keys.

```
sudo apt install xbubble
./xbubble_run.sh
```
Then in another terminal
```
./xbubble_bindkeys.sh
```

# rawkey

Helper to get host keycodes and keysyms. Mostly useful on host for setting key bindings.
```
./rawkey.sh
```

# host_colorpicker

Helper to get color codes. Runs only on the host.
