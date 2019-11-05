#!/usr/bin/python3
import RPi.GPIO as GPIO
import board
import busio
import time

filter = 19

GPIO.setmode(GPIO.BCM)
GPIO.setup(filter, GPIO.OUT)
GPIO.setwarnings(False)

def startRelay(channel):
    GPIO.output(channel, GPIO.LOW)

def stopRelay(channel):
    GPIO.output(channel, GPIO.HIGH)

startRelay(filter)
