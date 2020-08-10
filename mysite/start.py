# Threading Imports
import threading
from time import sleep
import time
from .statusLcd import lcd
from .sound import sound
from .singlethread import singlethread

# Creating the single thread
singlethread = threading.Thread(target=singlethread, daemon=True)
singlethread.start()

# Creating the status thread
lcdStatusThread = threading.Thread(target=lcd, daemon=True)
lcdStatusThread.start()
#
soundThread = threading.Thread(target=sound, daemon=True)
soundThread.start()
