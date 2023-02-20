import serial 
from roboclaw_3 import Roboclaw
from pynput import keyboard

port = "/dev/ttyTHS1" 
baudrate = 115200
address = 0x80 
timeout = 1
self.rate = rate

speedM1 = 0
speedM2 = 0 


ser = serial.Serial(port=port, rate,  baudrate=baudrate, timeout = timeout)
roboclaw_3 = Roboclaw(ser)

roboclaw_3.Open() 

def on_press(key):
    global speedM1, speedM2 

    try:
        if key.char == 'w':
            speedM1 = min(speedM1 + 100, 32767)
        elif key.char =='s':
            speedM1 = max(speedM1 - 100, -32767)
        elif key.char == 'e':
            speedM2 = min(speedM2 + 100, 32767)
        elif key.char == 'd': 
            speedM2 = max(speedM2 - 100, -32767)
        elif key.char == 'x': 
            speedM1 = 0
            speedM2 = 0     

        else: 
            return 
    except AttributeError: 
        return 
    

roboclaw_3 = Roboclaw(port, baudrate)


roboclaw_3.ForwardM1(address, speedM1)
roboclaw_3.ForwardM2(address, speedM2)

listner = keyboard.listner(on_press=on_press)
listner.start() 

listner.join() 

roboclaw_3.Close() 

