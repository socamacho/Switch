import board
import neopixel
from adafruit_circuitplayground import cp

cp.pixels.brightness = 0.3


while True:
    if cp.switch:
        cp.pixels[0] = (255, 0, 0)
        cp.pixels[1] = (0, 0, 255)
        cp.pixels[2] = (255, 150, 0)
        cp.pixels [3] = (0, 255, 0)
        cp.pixels [4] = (0, 255, 255)
        cp.pixels [5] = (180, 0, 255)


