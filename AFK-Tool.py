import pydirectinput
import pyautogui
import keyboard
from time import sleep
from os import system, name, listdir
from threading import Thread

clear = 'cls' if name == 'nt' else 'clear'

def load(): # Loading Animation
    print("Created By:  r       ")
    sleep(0.15)
    system(clear)
    print("Created By:  r c     ")
    sleep(0.15)
    system(clear)
    print("Created By: Cr c     ")
    sleep(0.15)
    system(clear)
    print("Created By: Cr c    8")
    sleep(0.15)
    system(clear)
    print("Created By: Cr c  2 8")
    sleep(0.15)
    system(clear)
    print("Created By: Crac  2 8")
    sleep(0.15)
    system(clear)
    print("Created By: Crac o2 8")
    sleep(0.15)
    system(clear)
    print("Created By: Crac o298")
    sleep(0.15)
    system(clear)
    print("Created By: Cracko298")
    sleep(2)

load()
print(" ")
print("Press 'Enter' To Run The Script.")
print("Press 'Ctrl' To Exit The Script.")
print(" ")

keyboard.wait('Enter')
print("Started Script...")

while keyboard.is_pressed('Ctrl') != True:
    print("Running check")
    afkList = []
    for img in listdir("imgs"):
        afkList.append(pyautogui.locateCenterOnScreen(f"imgs/{img}", confidence=0.9))

    for found in afkList:
        print(found, afkList)
        if found != None:
            pyautogui.moveTo(found)
            x,y = pyautogui.position()
            pydirectinput.moveTo(x+5,y)
            pydirectinput.click(x,y)