from ws2801 import TimPixels
from timcolor import TimColor
import time

first = TimPixels(50)
odd = TimColor(255, 0, 255)
even = TimColor(255, 255, 0)

black = TimColor(0, 0, 0)
white = TimColor(255, 255, 255)

first.RainbowCycle(0.05)
first.ClearLights()
time.sleep(1)

flashDelay = 0.25
first.Flash(odd, even, flashDelay, 100)
first.Flash(white, black, flashDelay, 100)

for i in range(len(first.pixels)):
    first.ToggleLight(i, even, 0.05)
