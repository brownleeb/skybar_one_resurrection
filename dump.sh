#!/bin/sh
# install to /usr/local/bin
gpio write 2 1
gpio write 3 1
sleep 5
gpio write 2 0
gpio write 3 0

