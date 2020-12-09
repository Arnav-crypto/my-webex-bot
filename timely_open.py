from datetime import datetime
import time
import webbrowser
from pynput.keyboard import Controller, Key

print("sucessfully initialized")
keyboard = Controller()
now = datetime.now()
print("everything good till now")
class1 = '15:31:00'

while True:
    current_time = now.strftime("%H:%M:%S")
    time.sleep(1)
    if current_time == class1 or class2 or class3 or class4 or class5:
        webbrowser.open(https://meetingsapac27.webex.com/meet/pr1668878079)
        time.sleep(6)
        keyboard.press(Key.enter)
    else:
        print("its not time yet its just " + current_time) 




