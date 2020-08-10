import RPi.GPIO as GPIO
import pyrebase

config = {
    "apiKey": "AIzaSyDhinRkAu5k-3aL83EIe_thcTwhmu1fVvU",
    "authDomain": "baby-156b1.firebaseapp.com",
    "databaseURL": "https://baby-156b1.firebaseio.com",
    "storageBucket": "baby-156b1.appspot.com",
    "serviceAccount": "firebase.json"
}
firebase = pyrebase.initialize_app(config)
db = firebase.database()
# _____________________________________
 #Chip Setup
in2 = 20
en2 = 21
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(en2, GPIO.OUT)
GPIO.setup(in2, GPIO.OUT)
p2 = GPIO.PWM(en2, 1000)
p2.start(50)
# _____________________________________



def fan():
    # if server is running
    control2 = db.child("Fan/run").get()
    level2 = db.child("Fan/level").get()

    if (control2.val()==0):
        GPIO.output(in2, 0)
        
    elif (level2.val()==1):
        p2.ChangeDutyCycle(50)
        GPIO.output(in2, 1)
        
    elif (level2.val()==2):
        p2.ChangeDutyCycle(75)
        GPIO.output(in2, 1)
        
    elif (level2.val()==3):
        p2.ChangeDutyCycle(100)
        GPIO.output(in2, 1)    
            
