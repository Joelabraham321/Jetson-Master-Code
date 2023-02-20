from roboclaw_3 import Roboclaw
import time 
from pynput import keyboard
import serial


serial_port = serial.Serial(
    port="/dev/ttyTHS1",
    baudrate=115200,
    bytesize=serial.EIGHTBITS,
    parity=serial.PARITY_NONE,
    stopbits=serial.STOPBITS_ONE,
)

if __name__ == "__main__":
    address1 = 0x80
    address2 = 0x81
    roboclaw_3 = Roboclaw("/dev/ttyTHS2", 115200)
    roboclaw_3.Open()

def on_press(key):
    if key.char == "w":
        #roboclaw_3.SpeedAccelM1M2(address,0, 1000, 1000)
        #roboclaw_3.ForwardM2(address, 127)
        roboclaw_3.SpeedM1(address1, 2500)
        roboclaw_3.SpeedM2(address1, 2500)

        # second motor controller 
        #roboclaw_3.SpeedM1(address2, 2500)
        #roboclaw_3.SpeedM2(address2, 2500)

        print ("w is pressed")
    #if key.char == "s":
        #roboclaw_3.SpeedM1(address, -2500)
        #roboclaw_3.SpeedM2(address, -2500)
        #print("s is pressed")
    #except AttributeError:
        #print("special key {0} pressed".format(
           # key))
    

def on_release(key):
    #print('{0} released'.format(
       # key)) 
    if key.char == "w":
        #time.sleep(2)
        roboclaw_3.SpeedM1(address1, 0)
        roboclaw_3.SpeedM2(address1, 0)

        # second motor controller 
        roboclaw_3.SpeedM1(address2, 0)
        roboclaw_3.SpeedM2(address2, 0)
    
# Collect events until released
with keyboard.Listener(
        on_press=on_press,
       on_release=on_release) as listener:
    listener.join()

# ...or, in a non-blocking fashion:
listener = keyboard.Listener(
    on_press=on_press,
    on_release=on_release)
listener.start()