import time
import usb_hid
from adafruit_hid.mouse import Mouse
import board
import digitalio as digitalIO

mouse = Mouse(usb_hid.devices)
switch = False

# set the button
btn = digitalIO.DigitalInOut(board.GP15)
btn.direction = digitalIO.Direction.INPUT
btn.pull = digitalIO.Pull.DOWN

led = digitalIO.DigitalInOut(board.GP25)
led.direction = digitalIO.Direction.OUTPUT
pixels_to_move = 30

#initialize led value as false
led.value = False
#time.sleep(3)

def move(is_left=False):
    global switch
    counter = 0
    multiplier = 1
    if btn.value:
        switch = not switch
    print(switch)
    if switch:
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
    print("__________________")


while True:
            # move mouse to right
            move()
            time.sleep(1)
            # move mouse to left
            move(True)
            time.sleep(1)
