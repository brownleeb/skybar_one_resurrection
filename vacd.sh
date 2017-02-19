#!/bin/sh
# install to /usr/local/bin
while :
do
   vac=$(cat /run/vac)
   empty="/srv/http/no_bottle"
   if [ $vac -gt 7200 -a ! -f $empty ]
   then
      /usr/local/bin/vacuum.py
   fi
   sleep 15m
done
