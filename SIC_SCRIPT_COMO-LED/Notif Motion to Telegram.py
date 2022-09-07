import telepot
import RPi.GPIO as GPIO
import time
from time import sleep
import datetime
from telepot.loop import MessageLoop
from subprocess import call

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(21, GPIO.IN)

motion = 0
motionNew = 0

def handle(msg):
    global telegramText
    global chat_id

    chat_id = msg['chat']['id']
    telegramText = msg['text']

    print('Message received from ' + str(chat_id))

    if telegramText == '/start':
        bot.sendMessage(chat_id, 'Security camera is activated.')#Put your welcome note here

    while True:
        main()


bot = telepot.Bot('5699892086:AAFltdBdSirRuquYf86RU-3rpRcCshqMe9g')
bot.message_loop(handle)

def main():

    global chat_id
    global motion

    while GPIO.input(21) == 1:
        print("Motion detected")
        motion = 1
        if motionNew != motion:
            sendNotification(motion)

def sendNotification(motion):
    global chat_id
    if motion == 1:
        bot.sendMessage(chat_id, 'Ada Pergerakan coba Cek CCTV!')
while 1:
    time.sleep(1)