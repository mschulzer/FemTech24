import random
import time
from machine import Pin, ADC, PWM
from neopixel import Neopixel
 
button = Pin(16, Pin.IN, Pin.PULL_UP)
btn_num = 0
pixels = Neopixel(5, 0, 0, "RGB") # no, state, pin, mode
adc = ADC(Pin(26, mode=Pin.IN))
my_rgb = (0, 0, 0)
 
while True:
    b1 = button.value()
    duty = adc.read_u16()
    scaled = int((duty / 65535) * 100)
    
    if not b1:
        x = list(my_rgb)		# Konverter tuple til liste
        x[btn_num] = scaled	# Ændr værdien på den pågældende plads
        my_rgb = tuple(x)	# Konverter liste tilbage til tuple
        
        if btn_num < 2:
            btn_num += 1
        else:
            btn_num = 0
            print(my_rgb)
            pixels.set_pixel(0, my_rgb)
            pixels.show()
        
        time.sleep(0.5)

