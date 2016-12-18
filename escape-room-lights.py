from socketIO_client import SocketIO
from ws2801 import TimPixels
from timcolor import TimColor
  
# url for websocket (dev and prod)
dev = 'http://10.0.0.2:5000'
prod = 'https://nameless-stream-30971.herokuapp.com'

# light control
pixels = TimPixels(50)
toggleDelay = 1

# here we are going to setup a dictionary to store
# and index and color for every letter.  
letters = {
    'A': [38, pixels.cBlue],
    'B': [39, pixels.cFuchsia],
    'C': [40, pixels.cGreen],
    'D': [41, pixels.cRed],
    'E': [43, pixels.cWhite],
    'F': [44, pixels.cYellow],
    'G': [45, pixels.cBlue],
    'H': [46, pixels.cFuchsia],
    'I': [48, pixels.cGreen],
    'J': [34, pixels.cRed],
    'K': [32, pixels.cWhite],
    'L': [30, pixels.cYellow],
    'M': [28, pixels.cBlue],
    'N': [27, pixels.cFuchsia],
    'O': [26, pixels.cGreen],
    'P': [25, pixels.cRed],
    'Q': [24, pixels.cWhite],
    'R': [9, pixels.cYellow],
    'S': [10, pixels.cBlue],
    'T': [11, pixels.cFuchsia],
    'U': [12, pixels.cGreen],
    'V': [13, pixels.cRed],
    'W': [15, pixels.cWhite],
    'X': [17, pixels.cYellow],
    'Y': [19, pixels.cBlue],
    'Z': [20, pixels.cFuchsia]}

# function to call when connected to websocket
# print the status of switch (returned) and status message
def on_connect(switch):
    print(switch)
    print('connected')
    pixels.Chase(pixels.demoColors, 6, 5, 0.005)
    pixels.Flash(pixels.cRed, pixels.cGreen, 0.05, 5)
    pixels.Flash(pixels.cRed, pixels.cGreen, 0.10, 5)
    pixels.Flash(pixels.cRed, pixels.cGreen, 0.25, 5)
    pixels.ClearLights()
    
# function to call when websocket emits 'letter' event
# this is where we want to toggle selected light
def on_letter(data):
    letter = data['letter']
    info = letters[letter]
    pixels.ToggleLight(info[0], info[1], toggleDelay)
    
# create websocket client and wait
# close spidev if keyboard interupt
try:
    socketIO = SocketIO(prod)
    socketIO.on('connected', on_connect)
    socketIO.on('letter', on_letter)
    socketIO.wait()

except KeyboardInterrupt:
    print('exit')
