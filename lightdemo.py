from ws2801 import TimPixels
from timcolor import TimColor
import time, sys

pixels = TimPixels(50)

try:
    while True:
        #pixels.LightDemo()
        pixels.RainbowCycle(0.005)
except KeyboardInterrupt:
    pixels.ClearLights()

