#import
import firebase_admin 
from firebase_admin import messaging
from firebase_admin import credentials
import pyrebase
from time import sleep

config = {
  "apiKey": "AIzaSyDhinRkAu5k-3aL83EIe_thcTwhmu1fVvU",
  "authDomain": "baby-156b1.firebaseapp.com",
  "databaseURL": "https://baby-156b1.firebaseio.com",
  "storageBucket": "baby-156b1.appspot.com",
   "serviceAccount": "firebase.json"
}

firebase = pyrebase.initialize_app(config)
db = firebase.database()


# TODO: Change config destination

cred = credentials.Certificate("/home/pi/Desktop/iot/mysite/baby-156b1-firebase-adminsdk-4hrde-8b3be05e37.json")
firebase_admin.initialize_app(cred)

token = "dsl2w_e-YXw:APA91bHALeraWNMHikgagRo9BlKr572uKiIfbfDFu4QjUKC27j1FLjjppq9WmawEdHv33PJbdk8WrsFU31QknlqBvKgHpZVp1H4Fb7mJNRtuPYo5Mkobx3ZBnst2HtYdg_cQcs0ti3rd"
image = "https://scontent-hbe1-1.xx.fbcdn.net/v/t1.0-9/100748026_2772019616236036_4724482090232446976_o.jpg?_nc_cat=104&_nc_sid=09cbfe&_nc_oc=AQluG9HeH0k7sxj8pa9BBcPTFNZxOj65itN2gnuN9DhLjmkMtNyQuKo1w1ZYSRg6u_I&_nc_ht=scontent-hbe1-1.xx&oh=19e24ff8a0297de87b889e68816bfd12&oe=5F0AF445"

def sendNotification(_title="title", _body="body",_image=image,_token=token):    
    notification = messaging.Notification(title=_title, body= _body, image=_image)        
    messages =[
        messaging.Message(
            notification=notification,
            token=_token,            
        ),
    ]
    response = messaging.send_all(messages)
    # store the response in the firebase database
    db.child("response/succsess").set(response.success_count)
    db.child("response/faliuer").set(response.failure_count)
