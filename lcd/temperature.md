# Obtaining a temperature reading
The temperature sensor that comes with the Pico is connected to one of a few special pins called ADCs or Analog-to-Digital Converters. The difference between a standard GPIO pin and an ADC pin is that a GPIO pin supports only two states, high and low, while an ADC pin supports a range of values, which is determined by the input voltage applied to the pin.

In the Pico, the ADC pins support 12-bits, which means that their value can go from 0 to 4095. MicroPython, however, scales the ADC values to a 16-bit range, so effectively the range is from 0 to 65535. The microcontroller runs at 3.3 V, which means that an ADC pin will return a value of 65535 when 3.3 V are applied to it, or 0 when there is no voltage. All the values in between are obtained when the voltage applied to the pin is between 0 and 3.3 V.

The ADC pins in the Pico board use their own numbering scheme instead of going by their GPIO pin number. In the pin diagram above you can see the pins labeled ADC0, ADC1, ADC2 and ADC_VREF (technically ADC3), which are the four externally accessible ADC pins. The temperature sensor does not have a physical pin in the board, but is accessed as ADC4.

The machine module provides the ADC() class to work with ADC pins. The following code can be used to read the temperature sensor from the MicroPython shell:

```
from machine import ADC
temp_sensor = ADC(4)
temperature = temp_sensor.read_u16()
```

If you print the value of the temperature value you are going to get an integer number between 0 and 65535, as indicated above. This is not very useful as a temperature measurement, so you will probably want to convert this value either to the Celsius or Fahrenheit degree scales.

The temperature sensor works by delivering a voltage to the ADC4 pin that is proportional to the temperature. According to the specifications of this sensor, a temperature of 27 degrees Celsius delivers a voltage of 0.706 V, with each additional degree reducing the voltage by 1.721 mV, or 0.001721 V. Conversely, each degree below 27 degrees Celsius increases the voltage by the same amount. The first step in converting the 16-bit temperature is to convert it back to volts, which is done based on the 3.3 V maximum voltage used by the Pico board:

```
to_volts = 3.3 / 65535
temperature = temperature * to_volts
```

With this conversion the temperature value holds a value between 0 and 3.3. A second conversion is now necessary to bring the temperature to the Celsius scale:

```
celsius_degrees = 27 - (temperature - 0.706) / 0.001721
```


information from:
[https://www.twilio.com/blog/programming-raspberry-pi-pico-microcontroller-micropython](https://www.twilio.com/blog/programming-raspberry-pi-pico-microcontroller-micropython)