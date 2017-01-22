#!/bin/sh
# install to /usr/local/bin
while :
do
   vac=$(cat /run/vac)
   if [ $vac -gt 7200 ]
   then
      /usr/local/bin/vacuum.py
   fi
   sleep 15m
done
