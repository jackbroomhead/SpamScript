import pyautogui
import time
import pyttsx3

time.sleep(5)

engine = pyttsx3.init()
engine.setProperty('rate', 200)

f = open("USA.txt", 'r')
for word in f:
    #engine.runAndWait()
    #engine.say(word)

    pyautogui.typewrite(word)
    pyautogui.press("enter")

