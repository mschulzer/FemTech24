from neopixel import Neopixel
from machine import Pin, ADC, PWM
import time

pixels = Neopixel(5, 0, 0, "RGB") # no, state, pin, mode
adc = ADC(Pin(26, mode=Pin.IN))
#pwm_led = PWM(Pin(15,mode=Pin.OUT))
#pwm_led.freq(1_000)

while True:
    duty = adc.read_u16() #  between ~350-65535
    scaled = int((duty / 65535) * 100)
    pixels.set_pixel(0, (scaled, scaled, scaled))
    pixels.show()
    time.sleep_ms(50)
