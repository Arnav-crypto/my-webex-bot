new :


from datetime import datetime
import time
import pyttsx3 
import webbrowser
from pynput.keyboard import Controller, Key
import os
import sys 

engine = pyttsx3.init()

voices = engine.getProperty('voices')
engine.setProperty('voice', voices[len(voices)-1].id)

def say(audio):
    engine.say(audio)
    engine.runAndWait()


keyboard = Controller()
class1 = '08:28:00'
class2 = '09:38:00'
class3 = '10:48:00'
class4 = '11:48:00'
class5 = '1:00:00'

while True:
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    time.sleep(1)
    if current_time in [class1, class2, class3, class4, class5]:
        print("It's time!!")
        say("let\'s go!!" + "come on" + "i have started the meeting for u!")
        webbrowser.open('https://meetingsapac27.webex.com/meet/pr1668878079')
        time.sleep(25)
        keyboard.press(Key.enter)
    else:
        print(current_time)
