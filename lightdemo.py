from ws2801 import TimPixels
from timcolor import TimColor
import time

first = TimPixels(50)
odd = TimColor(255, 0, 255)
even = TimColor(255, 255, 0)

first.RainbowCycle(0.05)
first.ClearLights()
time.sleep(1)

first.AlternateLights(even, odd)
time.sleep(5)

for i in range(len(first.pixels)):
    first.ToggleLight(i, even, 0.05)
