import RPi.GPIO as GPIO 

import time 

servo_pin = 33
frequency = 50 

duty_min = 5
duty_max = 20 

GPIO.setmode(GPIO.BCM) 
GPIO.setup(servo_pin, GPIO.OUT)

pwm = GPIO.PWM (servo_pin, frequency)

pwm.start(duty_min)

pwm.ChangeDutyCycle(duty_min)

time.sleep(1) 

pwm.ChangeDutyCycle(duty_max)

pwm.stop() 
GPIO.cleanup
