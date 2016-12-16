from socketIO_client import SocketIO
from ws2801 import TimPixels
from timcolor import TimColor
  
# url for websocket (dev and prod)
dev = 'http://10.0.0.2:5000'
prod = 'https://nameless-stream-30971.herokuapp.com'

# light control
lights = TimPixels(50)
toggleDelay = 1

# here we are going to setup a dictionary to store
# and index and color for every letter.  
letters = {
    'A': [0, TimColor(255, 0, 0)],
    'B': [1, TimColor(0, 255, 0)],
    'C': [2, TimColor(0, 255, 0)],
    'D': [3, TimColor(0, 255, 0)],
    'E': [4, TimColor(0, 255, 0)],
    'F': [5, TimColor(0, 255, 0)],
    'G': [6, TimColor(0, 255, 0)],
    'H': [7, TimColor(0, 255, 0)],
    'I': [8, TimColor(0, 255, 0)],
    'J': [9, TimColor(0, 255, 0)],
    'K': [10, TimColor(0, 255, 0)],
    'L': [11, TimColor(0, 255, 0)],
    'M': [12, TimColor(0, 255, 0)],
    'N': [13, TimColor(0, 255, 0)],
    'O': [14, TimColor(0, 255, 0)],
    'P': [15, TimColor(0, 255, 0)],
    'Q': [16, TimColor(0, 255, 0)],
    'R': [17, TimColor(255, 0, 255)],
    'S': [18, TimColor(0, 255, 0)],
    'T': [19, TimColor(0, 255, 0)],
    'U': [20, TimColor(0, 255, 0)],
    'V': [21, TimColor(0, 255, 0)],
    'W': [22, TimColor(0, 255, 0)],
    'X': [23, TimColor(0, 255, 0)],
    'Y': [24, TimColor(0, 255, 0)],
    'Z': [25, TimColor(0, 255, 0)]}

# function to call when connected to websocket
# print the status of switch (returned) and status message
def on_connect(switch):
    print(switch)
    print('connected')

# function to call when websocket emits 'letter' event
# this is where we want to toggle selected light
def on_letter(data):
    letter = data['letter']
    info = letters[letter]
    lights.ToggleLight(info[0], info[1], toggleDelay)
    
# create websocket client and wait
# close spidev if keyboar interupt
try:
    socketIO = SocketIO(prod)
    socketIO.on('connected', on_connect)
    socketIO.on('letter', on_letter)
    socketIO.wait()

except KeyboardInterrupt:
    spi.close()
