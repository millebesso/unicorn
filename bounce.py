import unicornhat as uh
import time

uh.set_layout(uh.PHAT)
uh.brightness(0.5)

x = 0
y = 0
deltax = 1
deltay = 1

while True:
    uh.clear()
    x += deltax
    y += deltay

    uh.set_pixel(x, y, 0, 255, 0)

    if x == 7 or x == 0:
        deltax = -deltax
    if y == 3 or y == 0:
        deltay = -deltay    
    
    uh.show()

    time.sleep(0.1)

