#!/usr/bin/env python

import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)

touch_pin= 31

GPIO.setup(touch_pin, GPIO.IN)

while True:
   if GPIO.input(touch_pin) == 0:

    if GPIO.input(touch_pin) == 1:
