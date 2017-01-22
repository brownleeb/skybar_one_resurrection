#!/bin/sh
# install to /usr/local/bin
# add "@reboot /usr/local/bin/startup.sh" to crontab using 'crontab -e'

/usr/bin/sleep 5
/usr/local/bin/gpio mode 7 out
/usr/local/bin/gpio mode 0 out
/usr/local/bin/gpio mode 2 out
/usr/local/bin/gpio mode 3 out
/usr/local/bin/gpio mode 12 out
/usr/local/bin/gpio mode 13 out
/usr/local/bin/gpio mode 14 out
/usr/local/bin/gpio mode 30 out
/usr/local/bin/gpio mode 21 out
/usr/local/bin/gpio mode 22 out
/usr/local/bin/gpio mode 23 out
/usr/local/bin/gpio mode 24 out
/usr/local/bin/gpio mode 25 out
/usr/local/bin/gpio write 7 0
/usr/local/bin/gpio write 0 1
/usr/local/bin/gpio write 2 0
/usr/local/bin/gpio write 3 0
/usr/local/bin/gpio write 12 0
/usr/local/bin/gpio write 13 0
/usr/local/bin/gpio write 14 0
/usr/local/bin/gpio write 30 0
/usr/local/bin/gpio write 21 0
/usr/local/bin/gpio write 22 0
/usr/local/bin/gpio write 23 0
/usr/local/bin/gpio write 24 0
/usr/local/bin/gpio write 25 0
/usr/local/bin/temp_control.py &
/usr/local/bin/vacd.sh &
