import Jetson.GPIO as GPIO 

import time 

relay_pin = 7


# Set up the GPIO channel
GPIO.setmode(GPIO.BOARD) 
GPIO.setup(relay_pin, GPIO.OUT, initial=GPIO.HIGH) 

print("Press CTRL+C when you want the LED to stop blinking") 
# Blink the LED
key = input('w')
while key == 'w': 
  time.sleep(2) 
  GPIO.output(relay_pin, GPIO.HIGH) 
  print("LED is ON")
  time.sleep(2) 
  GPIO.output(relay_pin, GPIO.LOW)
  print("LED is OFF")