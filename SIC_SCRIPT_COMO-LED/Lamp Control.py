import RPi.GPIO as GPIO
import time
import requests
import random
import time

TOKEN = "BBFF-kRHIGdAciMTng4COfLp30Zixtn0XBz" # Assign your Ubidots Token
DEVICE = "como-led" # Assign the device label to obtain the variable
VARIABLE = "lamp" # Assign the variable label to obtain the variable value
DELAY = 1  # Delay in seconds
 
 
# Set mode BCM
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
# PIN connected to IN1
relay_pin = 20
 
#Type of PIN - output
GPIO.setup(relay_pin,GPIO.OUT)
def get_var(device, variable):
    try:
        url = "http://industrial.api.ubidots.com/"
        url = url + \
            "api/v1.6/devices/{0}/{1}/".format(device, variable)
        headers = {"X-Auth-Token": TOKEN, "Content-Type": "application/json"}
        req = requests.get(url=url, headers=headers)
        return req.json()['last_value']['value']
    except:
        pass 
try:
    while True:
        print(get_var(DEVICE, VARIABLE))
        time.sleep(DELAY)
        #set low
        if (get_var(DEVICE, VARIABLE)==1.0):
            print ("Setting low - LAMP ON")
            GPIO.output (relay_pin,GPIO.LOW)
        else:
            #set high
            print ("Setting high - LAMP OFF")
            GPIO.output (relay_pin, GPIO.HIGH)
        
except KeyboardInterrupt:
        GPIO.cleanup()
        print ("Bye")