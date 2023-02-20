#udevadm trigger
#systemctl disable nvgetty
#systemctl stop nvgetty

from roboclaw_3 import Roboclaw
import time 
import serial


# Wait a second to let the port initialize
time.sleep(2)

if __name__ == "__main__":
    
    address = 0x80
    roboclaw_3 = Roboclaw("/dev/ttyTHS2", 115200)
    roboclaw_3.Open()
i =1 
while i<4:
    time.sleep(2) 

    roboclaw_3.ForwardM1(address,127)
    
    time.sleep(5)

    roboclaw_3.ForwardM2(address, 127)

    time.sleep(2) 

    roboclaw_3.ForwardM1(address, 0)
    roboclaw_3.ForwardM2(address, 0)

    print(i) 

    i+=1
    if i == 4: 
        roboclaw_3.ForwardM1(address, 0)
        roboclaw_3.ForwardM2(address, 0)

    



