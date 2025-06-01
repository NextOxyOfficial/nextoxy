import firebase_admin
from firebase_admin import credentials, messaging
from pathlib import Path
import os

BASE_DIR = Path(__file__).resolve().parent
cert = 'ajkerpristha-firebase-adminsdk-qe6wc-de7e0fd76f.json'
firebase_cred = credentials.Certificate(os.path.join(BASE_DIR, cert))
firebase_app = firebase_admin.initialize_app(firebase_cred)



def push(tokens, message):
    msg = messaging.MulticastMessage(
        notification=messaging.Notification(
            title=message['title'],
            body=message['text'],
        ),
    tokens=tokens
    )
    messaging.send_multicast(msg)