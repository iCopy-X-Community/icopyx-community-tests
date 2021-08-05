#!/bin/bash

NAME=$(basename $0)
NAME=${NAME%.sh}
if uname -a|grep -q NanoPi; then
    pgrep ipk_starter >/dev/null && sudo service icopy stop
    DISPLAY=:0 sudo xinit /usr/games/xbubble -s 13 -f 25
else
    xbubble -s 50 -f 25
fi
