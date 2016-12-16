from timcolor import TimColor
import spidev, time

# this class is used to control ws2801 addressable LEDs connected
# to a raspberry pi 3.  Connect clock to pin 23, connect data to pin 19
class TimPixels:

    # this is ran after the object is instantiated
    def __init__(self, numberOfPixels):
        self.numberOfPixels = numberOfPixels

        # intialize an empty list an append
        # TimColor objects based on numberOfPixels
        self.pixels = list()
        for i in range(numberOfPixels):
            self.pixels.append(TimColor(0, 0, 0))

        # initialize spi and open
        self.spi = spidev.SpiDev()
        self.spi.open(0, 0)

    # clean up when class is destroyed
    def __del__(self):
        self.spi.close()


    # function that can be used to set a color of a pixel
    def SetPixelColor(self, pixelIndex, color):
        self.pixels[pixelIndex] = color

    
    # function to write current pixel state to lights
    def UpdateLights(self):
        data = list()
        for i in range(len(self.pixels)):
            data.append(self.pixels[i].red)
            data.append(self.pixels[i].green)
            data.append(self.pixels[i].blue)
        self.spi.xfer(data)
            #self.spi.xfer2([self.pixels[i].red])
            #self.spi.xfer2([self.pixels[i].green])
            #self.spi.xfer2([self.pixels[i].blue])

    # function to clear all lights to off
    def ClearLights(self):
        for i in range(len(self.pixels)):
            self.SetPixelColor(i, TimColor(0, 0, 0))
        self.UpdateLights()

    # function to set every other light
    # can do odd and even at the same time
    def AlternateLights(self, evenColor, oddColor):
        for i in range(len(self.pixels)):
            if i % 2 == 0:
                self.SetPixelColor(i, evenColor)
            else:
                self.SetPixelColor(i, oddColor)
        self.UpdateLights()

    # function to turn on one light, wait and then turn it off
    # all other lights are turned off
    # this will be the main function for escape room
    def ToggleLight(self, i, color, delay):
        for x in range(len(self.pixels)):
            if x == i:
                self.SetPixelColor(x, color)
            else:
                self.SetPixelColor(x, TimColor(0, 0, 0))
        self.UpdateLights()
        time.sleep(delay)
        self.ClearLights()
                


                               

                               
