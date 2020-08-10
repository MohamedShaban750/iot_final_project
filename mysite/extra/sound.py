import RPi.GPIO as GPIO
import time
import pyrebase
from time import sleep
from .cloudMessaging import sendNotification
config = {
  "apiKey": "AIzaSyDhinRkAu5k-3aL83EIe_thcTwhmu1fVvU",
  "authDomain": "baby-156b1.firebaseapp.com",
  "databaseURL": "https://baby-156b1.firebaseio.com",
  "storageBucket": "baby-156b1.appspot.com",
   "serviceAccount": "firebase.json"
}

firebase = pyrebase.initialize_app(config)
db = firebase.database()

#GPIO SETUP
channel = 12
GPIO.setmode(GPIO.BCM)
GPIO.setup(channel, GPIO.IN)

def callback(channel):
    if GPIO.input(channel):
        db.child("Sound Detection/detected").set("yes") 
    else:
        db.child("Sound Detection/detected").set("yes")
        
# let us know when the pin goes HIGH or LOW
GPIO.add_event_detect(channel, GPIO.BOTH, bouncetime=300)
# assign function to GPIO PIN, Run function on change
GPIO.add_event_callback(channel, callback)  

# infinite loop
def sound():
    sound = db.child("Sound Detection/detected").get()    
    if (sound.val()=="yes"):   
        time.sleep(5)
        sendNotification(
        "ابنك بيعيط ياختي",
        "روحي نيمي ابنك يا وليه!")
        time.sleep(5)
        db.child("Sound Detection/detected").set("no")
