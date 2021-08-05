#!/bin/bash

NAME=$(basename $0)
NAME=${NAME%.sh}
if uname -a|grep -q NanoPi; then
    pgrep ipk_starter >/dev/null && sudo service icopy stop
    DISPLAY=:0 sudo python3 $NAME.py
else
    echo "Cannot run on host"
    exit 1
fi
