from machine import Pin, Timer

led1 = Pin(2, Pin.OUT)
led2 = Pin(20, Pin.OUT)

LED_state1 = True
LED_state2 = False

tim = Timer()

def tick(timer):
    global led1, led2, LED_state1, LED_state2
    LED_state1 = not LED_state1
    LED_state2 = not LED_state2
    led1.value(LED_state1)
    led2.value(LED_state2)
    
tim.init(freq=9, mode=Timer.PERIODIC, callback=tick)