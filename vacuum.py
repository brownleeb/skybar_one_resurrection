#!/usr/bin/python
# Install to /usr/local/bin
import time
import syslog
import RPi.GPIO as GPIO

from subprocess import call
# Import the ADS1x15 module.
import Adafruit_ADS1x15

# Create an ADS1115 ADC (16-bit) instance.
adc = Adafruit_ADS1x15.ADS1115()
RELAY_4 = 13
PUMP = 37

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(RELAY_4, GPIO.OUT)
GPIO.setup(PUMP, GPIO.OUT)
GPIO.output(PUMP, True)
GPIO.output(RELAY_4, True)
GAIN = 1
vac= adc.read_adc(1, gain=GAIN)
# Main loop.
while (vac > 7100):
 try:
    time.sleep(0.5)
    vac = adc.read_adc(1, gain=GAIN)

 except Exception as ex:
    template = "An exception of type {0} occured. Arguments:\n{1!r}"
    message = template.format(type(ex).__name__, ex.args)
    syslog.syslog(message)

GPIO.output(RELAY_4, False)
GPIO.output(PUMP, False)
