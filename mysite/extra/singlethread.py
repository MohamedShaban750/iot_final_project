from .motor import motor
from .fan import fan
from .play import music
def singlethread():
    # While server is running
    i = 0
    while(True):
        motor()
        fan()
        music()
    # Once server is closed    
    GPIO.cleanup()        

