import utime, time

import machine
from machine import I2C
from lcd_api import LcdApi
from pico_i2c_lcd import I2cLcd

# this is the address of the i2c screen
I2C_ADDR     = 0x27
# number of rows
I2C_NUM_ROWS = 2
# number of columns
I2C_NUM_COLS = 16

# new instances
i2c = I2C(0, sda=machine.Pin(0), scl=machine.Pin(1), freq=400000)
lcd = I2cLcd(i2c, I2C_ADDR, I2C_NUM_ROWS, I2C_NUM_COLS)

# clear the screen
lcd.clear()

# Print temp: on the position 1,0
lcd.putstr("Temp: ")

while True:
    # lets move the cursor to the position 7 on the fist line to write the values
    lcd.move_to(7,0)

    # get the temperature from the internal sensor of the pico
    # explanation on temperature.md file
    sensor_temp = machine.ADC(4)
    conversion_factor = 3.3/(65535)
    reading = sensor_temp.read_u16() * conversion_factor
    temperature = 27 - (reading - 0.706)/0.001721

    # rounding the value of the temperature
    lcd.putstr(str(round(temperature, 1)))
    lcd.putchar(' ')

    # print the ° character
    lcd.putchar('\xdf')
    lcd.putchar("C")

    # sleep 1 minute before next reading
    time.sleep(60)

