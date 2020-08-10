import pygame
import pyrebase
import time
from time import sleep

config = {
  "apiKey": "AIzaSyDhinRkAu5k-3aL83EIe_thcTwhmu1fVvU",
  "authDomain": "baby-156b1.firebaseapp.com",
  "databaseURL": "https://baby-156b1.firebaseio.com",
  "storageBucket": "baby-156b1.appspot.com",
   "serviceAccount":  "firebase.json"
}

firebase = pyrebase.initialize_app(config)
db = firebase.database()

pygame.mixer.init()
s=pygame.mixer.music

#play = db.child("play").get()
musicPath = "/home/pi/Desktop/iot/mysite/"
def music():
    song = db.child("Music/song").get()
    if (song.val()==1):
        s.load(musicPath +"1.mp3")
        s.play()
        db.child("Music/song").set(7)
        if (song.val()==7):
            pygame.mixer.music.get_busy()
    elif (song.val()==2):
        s.load(musicPath +"2.mp3")
        s.play()
        db.child("Music/song").set(7)
        if (song.val()==7):
            pygame.mixer.music.get_busy()

    elif (song.val()==3):
        s.load(musicPath +"2.mp3")
        s.play()
        db.child("Music/song").set(7)
        if (song.val()==7):
            pygame.mixer.music.get_busy()

    elif (song.val()==4):
        s.load(musicPath +"2.mp3")
        s.play()
        db.child("Music/song").set(7)
        if (song.val()==7):
            pygame.mixer.music.get_busy()
            
    elif (song.val()==5):
        s.load(musicPath +"2.mp3")
        s.play()
        db.child("Music/song").set(7)
        if (song.val()==7):
            pygame.mixer.music.get_busy()
   
    elif (song.val()==0):
        pygame.mixer.music.stop()

    
