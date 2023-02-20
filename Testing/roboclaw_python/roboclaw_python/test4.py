from sshkeyboard import listen_keyboard
from roboclaw_3 import Roboclaw
import time 
import serial


serial_port = serial.Serial(
    port="/dev/ttyTHS1",
    baudrate=115200,
    bytesize=serial.EIGHTBITS,
    parity=serial.PARITY_NONE,
    stopbits=serial.STOPBITS_ONE,
)

if __name__ == "__main__":
    address = 0x80
    roboclaw_3 = Roboclaw("/dev/ttyTHS1", 115200)
    roboclaw_3.Open()


def press(key):
    
    if key == "w":
        roboclaw_3.ForwardM1(address, 127)
        roboclaw_3.ForwardM2(address, 127)
        print(f"'{key}' pressed")
    if key == "s":
        #roboclaw_3.SpeedM1(address, -2500)
        #roboclaw_3.SpeedM2(address, -2500)
        print(f"'{key}' pressed")

def release(key): 
    if key == "w":
        roboclaw_3.SpeedM1(address, 0)
        roboclaw_3.SpeedM2(address, 0)
        print(f"'{key}' released")
    if key == "s":
        #roboclaw_3.SpeedM1(address, 0)
        #roboclaw_3.SpeedM2(address, 0)
        print(f"'{key}' released")

listen_keyboard(
    on_press = press, 
    on_release = release, 

)