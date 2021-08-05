#!/bin/bash

NAME=$(basename $0)
NAME=${NAME%.sh}
if uname -a|grep -q NanoPi; then
    pgrep ipk_starter >/dev/null && sudo service icopy stop
    DISPLAY=:0 sudo xinit /usr/bin/python3 $NAME.py
else
    python3 $NAME.py
fi
