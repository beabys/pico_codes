import time
import usb_hid
from adafruit_hid.mouse import Mouse
import board
import digitalio as digitalIO

mouse = Mouse(usb_hid.devices)
led = digitalIO.DigitalInOut(board.GP25)
led.direction = digitalIO.Direction.OUTPUT

led.value = False
time.sleep(5)
mouse.move(y=400)

while True:
    click = 500
    while click > 0:
        led.value = True
        mouse.click(Mouse.LEFT_BUTTON)
        time.sleep(0.01)
        click = click -1
    led.value = False
    time.sleep(60)