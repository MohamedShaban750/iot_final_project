import firebase_admin 
from firebase_admin import messaging
from firebase_admin import credentials

# TODO: Change config destination
cred = credentials.Certificate("C:\\Users\\ahmed\Desktop\\cam\\cam\\baby-156b1-firebase-adminsdk-4hrde-8b3be05e37.json")
firebase_admin.initialize_app(cred)

token = "dtBy1n1byEU:APA91bGiPKRdPo_Ox_i27Du0pdwoUpS0G-2bAeWjVAlHIG1xRljF-KGgzxxo6f-Er_h8Pdzf1LEzXEbWJjv1rvcB9FC5h_ql6u9Y7Qubcor32h-rmu7xC57OReNJFvvYMCYDcyrbiLyq"

def sendNotification(_title="title", _body="body",_token=token,_image=''):    
    if(_image=="Temp"):
        notification = messaging.Notification(title=_title,
                body= _body, 
                image="حصورة الحرارة")        
    elif(_image=="Humidity"):
        notification = messaging.Notification(title=_title,
                body= _body, 
                image="صورة الرطوبه")
    else:
        notification = messaging.Notification(title=_title,
                body= _body,                 
                image="https://scontent-hbe1-1.xx.fbcdn.net/v/t1.0-9/100748026_2772019616236036_4724482090232446976_o.jpg?_nc_cat=104&_nc_sid=09cbfe&_nc_oc=AQluG9HeH0k7sxj8pa9BBcPTFNZxOj65itN2gnuN9DhLjmkMtNyQuKo1w1ZYSRg6u_I&_nc_ht=scontent-hbe1-1.xx&oh=19e24ff8a0297de87b889e68816bfd12&oe=5F0AF445")        
    token = _token
    messages = [
        messaging.Message(
            notification=notification,
            token=token,            
        ),
    ]
    response = messaging.send_all(messages)
