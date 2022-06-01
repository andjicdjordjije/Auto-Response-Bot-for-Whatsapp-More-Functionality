import pyautogui as pt
import shutil
import os
from time import sleep
import pyperclip
import random

sleep(3)

position1 = pt.locateOnScreen("smiley.png", confidence=.6)
x = position1[0]
y = position1[1]

#gets message
def get_message():
    global x,y

    postion = pt.locateOnScreen("smiley.png", confidence=.6)
    x = position1[0]
    y = position1[1]
    pt.moveTo(x,y, duration=.05)
    pt.moveTo(x + 70, y - 40, duration = .5)
    pt.tripleClick()
    pt.rightClick()
    pt.moveRel(12,15)
    pt.click()
    whatsapp_message = pyperclip.paste()
    pt.click()
    print("message received: " + whatsapp_message)

    return whatsapp_message

#posts
def post_response(message):
    global x, y

    position = pt.locateOnScreen("smiley.png", confidence=.6)
    x = position1[0]
    y = position1[1]
    pt.moveTo(x + 200, y + 20, duration=.5)
    pt.click()
    pt.typewrite(message, interval=.01)

    pt.typewrite("\n", interval=.01)

#process response
def process_response(message):
    random_no = random.randrange(3)

    if "?"in str(message).lower():
        return "Interesting question, I'll talk to you about that later - Bot Constantine"

    else:
        if "hi"in str(message).lower():

            return "Hey, a bit busy right now. just drop a message ill talk to you later- Bot Constantine"

        elif "happy new year"in str(message).lower():
            return "Wishing you and your family a very Happy New Year! ✨.May this year bring joy and happiness in your life! - Bot Constantine "
        elif "good morning"in str(message).lower():
            return"Good Morning! Have a great day"
        elif "good night"in str(message).lower():
            return"Good Night! Sleep tight"
        elif "analysis" in str(message).lower():
            return "http://www.africau.edu/images/default/sample.pdf"
        else :
            return "Hello! Dear Sir/Madam, Djole is currently unavailable to reply. Do drop your messages. - Bot Constantine"





#new messages check
def check_for_new_messages():
    pt.moveTo(x + 50, y - 45, duration=.5)

    while True:
        try:
            position = pt.locateOnScreen("circle.png", confidence = .7)

            if position is not None:
                pt.moveTo(position)
                pt.moveRel(-100,0)
                pt.click()
                processed_message = process_response(get_message())
                post_response(processed_message)
                with pt.hold('ctrlleft'):
                    with pt.hold('shift'):
                        pt.press('d')
                sleep(1)
                position = pt.locateOnScreen("deletechat.png", confidence=.6)
                pt.moveTo(position)
                pt.click()
                sleep(5)

            else:
                print("No messages")
                sleep(5)

        except(Exception):
            print("No new messages")





check_for_new_messages()
#processed_message = process_response(get_message())
#post_response(processed_message)
