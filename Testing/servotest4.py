import RPi.GPIO as GPIO 
from time import sleep

import gpiozero
from gpiozero.pins.mock import MockFactory
from gpiozero import Servo

gpiozero.Device.pin_factory = MockFactory()

servo = Servo(8)


try: 
	while True: 
		servo.min() 
		sleep(0.5)
except KeyboardInterrupt:
    print("Program stopped")