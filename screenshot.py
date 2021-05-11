import keyboard
import time
from PIL import ImageGrab

def screenshot():
    curr_time = time.strftime("_%Y%m%d_%H%M%S")
    img = ImageGrab.grab()
    img.save('image{}.png'.format(curr_time))

keyboard.add_hotkey('F9', screenshot)
# keyboard.add_hotkey('ctrl+shift+a', screenshot)

keyboard.wait('esc')