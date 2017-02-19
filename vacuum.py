#!/usr/bin/python

import time
import syslog, os
import RPi.GPIO as GPIO

from subprocess import call
import Adafruit_ADS1x15

adc = Adafruit_ADS1x15.ADS1115()
RELAY_4 = 13
PUMP = 37

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(RELAY_4, GPIO.OUT)
GPIO.setup(PUMP, GPIO.OUT)
GAIN = 1
start=time.time()
while ((adc.read_adc(1, gain=GAIN)) > 7100):
   GPIO.output(PUMP, True)
   GPIO.output(RELAY_4, True)
   time.sleep(0.5)
   if ((time.time() - start) > 10):
      open('/srv/http/no_bottle','a').close()
      break
GPIO.output(RELAY_4, False)
GPIO.output(PUMP, False)
