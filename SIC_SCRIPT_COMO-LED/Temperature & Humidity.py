import Adafruit_DHT
import time
import pyrebase


DHT_SENSOR = Adafruit_DHT.DHT11
DHT_PIN = 4

config = {
  "apiKey": "AIzaSyCbMHZOnmKtW3cOxiCFI3YrcSCEpLM4pg4",
  "authDomain": "dht11-cfe67.firebaseapp.com",
  "databaseURL": "https://dht11-cfe67-default-rtdb.firebaseio.com",
  "projectId": "dht11-cfe67",
  "storageBucket": "dht11-cfe67.appspot.com",
  "messagingSenderId": "323848534600",
  "appId": "1:323848534600:web:8983aa6d3b6280e975367d",
  "measurementId": "G-RK2596DNGG"
}

firebase = pyrebase.initialize_app(config)


print("Send Data to Firebase Using Raspberry Pi")
print("—————————————-")


while True:
    humidity, temperature = Adafruit_DHT.read_retry(DHT_SENSOR, DHT_PIN)
    if humidity is not None and temperature is not None:
        print("Temp={0:0.1f}*C  ={1:0.1f}%".format(temperature, humidity))
        storage = firebase.storage()
        database = firebase.database()

            
        database.child("dht11")
        data = {"Temp": temperature,                   
                "Humidity": humidity   }
        database.set(data)
        time.sleep(1)
    else:
        print("Failed to retrieve data from humidity sensor")
 
            
