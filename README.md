# Proxmark3 part

## Compiling upstream client

* https://github.com/iCopy-X-Community/icopyx-community-pm3 branch **master**
* `Makefile.platform`:
```
PLATFORM=PM3RDV4
STANDALONE=
```

## Compiling latest client

iCopy-X changes ported to current RRG master:

* https://github.com/iCopy-X-Community/icopyx-community-pm3 branch **icopyx-experimental**
* `Makefile.platform`:
```
PLATFORM=PM3ICOPYX
STANDALONE=
```

## Flashing Proxmark3

From host:
```
scp armsrc/obj/fullimage.elf root@192.168.x.x:/mnt/upan/
```
From iCopy-X:
```
sudo service icopy stop
sudo ipk_app_main/pm3/proxmark3 /dev/ttyACM0 --flash --image /mnt/upan/fullimage.elf
sudo service icopy start
```

## Driving Proxmark3 from host

From iCopy-X GUI: Start PC Mode

From host:

port must be explicit
```
client/proxmark3 /dev/ttyACM0
```

## Cross-compile client for armv7l

TODO:

# GUI tests

Binding HMI keys to X11 requires the following:
```
sudo apt install libxdo3 xdotool libxdo-dev
sudo python3 -m pip install python-libxdo
```
Displaying GUI on host properly requires the following on the host:
```
sudo apt install fonts-mononoki
```

See [libtests](libtests) for various examples and experiments.
