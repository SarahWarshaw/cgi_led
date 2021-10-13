#!/usr/bin/python3

# This code runs continually in the background to apply
# the stored PWM slider value to the GPIO output

import RPi.GPIO as gpio
import time

ledPin = 19

gpio.setmode(gpio.BCM)
gpio.setup(ledPin, gpio.OUT)

pwm = gpio.PWM(ledPin, 100) # PWM object on our pin at 100 Hz
pwm.start(0) # start with LED off

while True:
  with open("led-pwm.txt", 'r') as file:
    dutyCycle = float(file.read()) # read duty cycle value from file
  pwm.ChangeDutyCycle(dutyCycle)
  time.sleep(0.1)
