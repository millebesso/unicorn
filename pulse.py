import unicornhat as uh
import random
import time

uh.set_layout(uh.PHAT)
brightness_min = 0.25
brightness_max = 0.9
brightness_delta = 0.1
brightness = brightness_min

while True:
    for i in range(8):
        for j in range (4):        
            uh.set_pixel(i, j, 255, 0, 0)
            
    brightness += brightness_delta
    if brightness >  brightness_max:
        brightness_delta = -0.1
    if brightness < brightness_min:
        brightness_delta = 0.1

    uh.brightness(brightness)
    uh.show()

    time.sleep(0.1)

