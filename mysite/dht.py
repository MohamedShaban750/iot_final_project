# Threading Imports
import threading
from time import sleep
# _____________________________________
# Djanogo Imports
from django.shortcuts import render
from django.http import HttpResponse
# _____________________________________
import sys
import Adafruit_DHT
import time
import pyrebase
import firebase_admin
from firebase_admin import credentials
import RPi.GPIO as GPIO
# from firebase_admin import db


config = {
    "apiKey": "AIzaSyDhinRkAu5k-3aL83EIe_thcTwhmu1fVvU",
    "authDomain": "baby-156b1.firebaseapp.com",
    "databaseURL": "https://baby-156b1.firebaseio.com",
    "storageBucket": "baby-156b1.appspot.com",
    "serviceAccount": "firebase.json"
}

firebase = pyrebase.initialize_app(config)
db = firebase.database()

# data = {"tem": "",
#       "hum": ""}
# db.child("status").set(data)


# Humidity Threading Setup
Humidity_Running = True

# Thread Function


def readFirebaseDatabase():
    global Humidity_Running

    # if Humidity is running
    while(True):
        control = db.child("status/run").get()
        if(control.val() == True):
            humidity, temperature = Adafruit_DHT.read_retry(11, 4)
            # print 'Temp: {0:0.1f} C  Humidity: {1:0.1f} '.format(temperature, humidity)
            time.sleep(2)
            data = {"Humidity": ' %.1f ' %humidity, "Temperature": ' %.1f ' % temperature}
            db.child("status").set(data)


# Creating the motor thread
Humidity_Thread = threading.Thread(target=readFirebaseDatabase, daemon=True)
Humidity_Thread.start()

# # localhost:8000/sensors/on


# def open(request):
#     global Humidity_Running
#     Humidity_Running = True
#     return HttpResponse("Humidity sensor is runing...")

# # localhost:8000/sensors/off


# def close(request):
#     global Humidity_Running
#     Humidity_Running = False
#     return HttpResponse("Humidity sensor has stopped!")
