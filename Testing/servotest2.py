from piservo import Servo 

import time 

myservo = Servo(33)

myservo.write(180)

time.sleep(3) 

myservo.write(0)

time.sleep(3) 

myservo.stop()
