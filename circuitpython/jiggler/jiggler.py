import time
import usb_hid
from adafruit_hid.mouse import Mouse
import board
import digitalio as digitalIO

mouse = Mouse(usb_hid.devices)

led = digitalIO.DigitalInOut(board.GP25)
led.direction = digitalIO.Direction.OUTPUT
pixels_to_move = 30

#initialize led value as false
led.value = False
time.sleep(3)

def move(is_left=False):
    counter = 0
    multiplier = 1
    if is_left:
        multiplier = -1
    # led is on during execution
    led.value = True
    while counter <= pixels_to_move:
        counter += 1
        x_position = (counter) * multiplier
        mouse.move(x=x_position)
        time.sleep(0.01) 
    led.value = False

while True:
    # move mouse to right
    move()
    time.sleep(1)
    # move mouse to left
    move(True)
    time.sleep(1)
