import RPi.GPIO as GPIO 

import time 

servo_pin = 33

def main(): 

# Set up the GPIO channel
#    GPIO.setmode(GPIO.BOARD) 
#    GPIO.setup(servo_pin, GPIO.OUT, initial=GPIO.HIGH) 

#    print("Startinh Demo")

#    time.sleep(1)
#    curr_value = GPIO.HIGH

#    try: 
#        while True: 
#            time.sleep(1) 
#            GPIO.output(servo_pin, curr_value)
#           curr_value ^= GPIO.HIGH
#    finally: 
#        GPIO.cleanup()
#if __name__== 'main': 
#    main() 

    p = GPIO.PWM(servo_pin, 50) #50 Hz 

    p.start(2.5) 
    time.sleep(2) 
    GPIO.output(servo_pin, GPIO.HIGH) 
    time.sleep(2) 
    GPIO.output(servo_pin, GPIO.LOW)

    try:
        while True: 
            p.ChangeDutyCycle(5) 
            time.sleep(0.5) 

            p.ChangeDutyCycle(7.5) 
            time.sleep(0.5) 

    except KeyboardInterrupt: 
        p.stop() 
        GPIO.cleanup() 


