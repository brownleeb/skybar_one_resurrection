#!/usr/bin/python
# installed to /usr/local/bin

import time
import syslog
import sys
import RPi.GPIO as GPIO
import os
import Adafruit_ADS1x15
verbose=0
if len(sys.argv) == 2:
   if sys.argv[1] == "-v":
      verbose=1
      print('Verbose')

cool_GPIO = 7
fans_GPIO = 11
aux_fan_GPIO = 31
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(cool_GPIO, GPIO.OUT)
GPIO.setup(fans_GPIO, GPIO.OUT)
GPIO.setup(aux_fan_GPIO, GPIO.OUT)

no_bottle=False
cool=0
GPIO.output(cool_GPIO, False)

# Create an ADS1115 ADC (16-bit) instance.
adc = Adafruit_ADS1x15.ADS1115()

GAIN = 1

while True:
 try:
    if (os.path.exists('/srv/http/no_bottle')):
       GPIO.output(cool_GPIO, False)
       cool=0
       GPIO.output(fans_GPIO, False)
       GPIO.output(aux_fan_GPIO, False)
       no_bottle=True
       time.sleep(10.0)
    else:
       if (no_bottle):
          no_bottle=False
          GPIO.output(fans_GPIO, True)

       temp = adc.read_adc(0, gain=GAIN)
       vac = adc.read_adc(1, gain=GAIN)
       if (verbose == 1):
          print('| {0:>6} | {1:>6} |'.format(temp,vac))

       f=open("/srv/http/set_pt","r")
       set_pt=int(f.read())
       f.close()

       f=open("/run/temp","w")
       f.write(str(temp))
       f.close()

       f=open("/run/vac","w")
       f.write(str(vac))
       f.close()

       if (temp < (set_pt-50)) and (cool == 0):
          GPIO.output(cool_GPIO, True)
          cool=1
          if verbose == 1:
             print("Turning cooling on - " + str(temp))
       if (temp > (set_pt+50)) and (cool == 1):
          if verbose == 1:
             print("Turning cooling off - " + str(temp))
          cool=0
          GPIO.output(cool_GPIO, False)
       time.sleep(10.0)

 except Exception as ex:
    template = "An exception of type {0} occured. Arguments:\n{1!r}"
    message = template.format(type(ex).__name__, ex.args)
    syslog.syslog(message)
    time.sleep(10)
