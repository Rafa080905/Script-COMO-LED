import RPi.GPIO as GPIO  
GPIO.setmode(GPIO.BCM) 
GPIO.setup(21, GPIO.IN)
from datetime import datetime
from picamera import PiCamera
from time import sleep
import os

import pyrebase

firebaseConfig = {
  'apiKey': "AIzaSyCB-iFJoqtUUvu_SGxMYNfiZpp8y6Uvc-4",
  'authDomain': "kamera-452e9.firebaseapp.com",
  'databaseURL': "https://kamera-452e9-default-rtdb.firebaseio.com",
  'projectId': "kamera-452e9",
  'storageBucket': "kamera-452e9.appspot.com",
  'messagingSenderId': "668600036530",
  'appId': "1:668600036530:web:f49d06e9d8c199fe8a6dab",
  'measurementId': "G-ET7SH08KTG"

}

firebase = pyrebase.initialize_app(firebaseConfig)

storage = firebase.storage()
camera = PiCamera()
while True: 
  try:
    if GPIO.input(21) == 1:
        
        print("Detect")
        now = datetime.now()
        dt = now.strftime("%d%m%Y%H:%M:%S")
        name = dt+".jpg"
        camera.capture(name)
        print(name+" saved")
        storage.child(name).put(name)
        print("Image sent")
        os.remove(name)
        print("File Removed")
        sleep(2)
        
  except:
      if GPIO.input(21) == 0:
      camera.close()  