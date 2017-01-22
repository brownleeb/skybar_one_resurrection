#!/usr/bin/python
# install to /srv/http
import time
import RPi.GPIO as GPIO
import sys
RELAY_1 = 35
RELAY_2 = 33
RELAY_3 = 15
RELAY_4 = 13
PUMP = 37
if sys.argv[1] == "2":
      DELAY = 4.5
elif sys.argv[1] == "3":
      DELAY = 6.0
elif sys.argv[1] == "4":
      DELAY = 8.0
elif sys.argv[1] == "5":
      DELAY = 10.0
elif sys.argv[1] == "6":
      DELAY = 11.5
else:
      print ("Error in pour size")
      sys.exit(1)
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(RELAY_1, GPIO.OUT)
GPIO.setup(RELAY_2, GPIO.OUT)
GPIO.setup(RELAY_3, GPIO.OUT)
GPIO.setup(RELAY_4, GPIO.OUT)
GPIO.setup(PUMP, GPIO.OUT)
GPIO.output(RELAY_3, True)
GPIO.output(RELAY_4, True)
time.sleep(2.5)
GPIO.output(RELAY_3, False)
GPIO.output(RELAY_1, True)
GPIO.output(RELAY_2, True)
GPIO.output(PUMP, True)
time.sleep(DELAY)
GPIO.output(PUMP, False)
GPIO.output(RELAY_3, True)
GPIO.output(RELAY_2, False)
GPIO.output(RELAY_1, False)
time.sleep(4)
GPIO.output(RELAY_3, False)
GPIO.output(RELAY_4, False)
call(["sudo /usr/local/bin/vacuum.py"])
