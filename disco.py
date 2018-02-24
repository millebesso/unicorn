import unicornhat as uh
import random
import time

uh.set_layout(uh.PHAT)
uh.brightness(0.5)


while True:
    for i in range(8):
        for j in range (4):
            r = random.randint(0, 255)
            g = random.randint(0, 255)
            b = random.randint(0, 255)
        
            uh.set_pixel(i, j, r, g, b)

    uh.show()

    time.sleep(0.5)

