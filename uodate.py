import pydirectinput
import pyautogui
import keyboard
import time
from os import system, path

check_win = path.exists("C:\Windows\SysWOW64") # Linux or Windows Detection Basically
if check_win == True:
  clear = 'cls'
else:
  clear = 'clear'

print("Press 'Enter' To Run The Script.")
print("Press 'Ctrl' To Exit The Script.")
print(" ")

keyboard.wait('Enter')
print("Started Script...")

lastTime = 0
stopAll = False

def toggle():
    global stopAll
    stopAll = not stopAll
    print(stopAll)

keyboard.add_hotkey('j', toggle)

while keyboard.is_pressed('Ctrl') != True:
    afk0 = pyautogui.locateCenterOnScreen('_afk0.png', confidence=0.9)
    afk1 = pyautogui.locateCenterOnScreen('_afk1.png', confidence=0.9)
    afk3 = pyautogui.locateCenterOnScreen('_afk3.png', confidence=0.9)
    afk4 = pyautogui.locateCenterOnScreen('_afk4.png', confidence=0.9)
    afk5 = pyautogui.locateCenterOnScreen('_afk5.png', confidence=0.9)
    afk6 = pyautogui.locateCenterOnScreen('_afk01.png', confidence=0.9)
    shouldMove = True

    if afk0 != None:
        pyautogui.moveTo(afk0)
        x,y = pyautogui.position()
        pydirectinput.moveTo(x+5,y)
        pydirectinput.click(x,y)
        shouldMove = False
    
    if afk1 != None:
        pyautogui.moveTo(afk1)
        x,y = pyautogui.position()
        pydirectinput.moveTo(x+5,y)
        pydirectinput.click(x,y)
        shouldMove = False

    if afk3 != None:
        pyautogui.moveTo(afk3)
        x,y = pyautogui.position()
        pydirectinput.moveTo(x+5,y)
        pydirectinput.click(x,y)
        shouldMove = False

    if afk4 != None:
        pyautogui.moveTo(afk4)
        x,y = pyautogui.position()
        pydirectinput.moveTo(x+5,y)
        pydirectinput.click(x,y)
        shouldMove = False

    if afk5 != None:
        pyautogui.moveTo(afk5)
        x,y = pyautogui.position()
        pydirectinput.moveTo(x+5,y)
        pydirectinput.click(x,y)
        shouldMove = False

    if afk6 != None:
        pyautogui.moveTo(afk6)
        x,y = pyautogui.position()
        pydirectinput.moveTo(x+5,y)
        pydirectinput.click(x,y)
        shouldMove = False

    print(time.time() - lastTime)

    if not stopAll:
        if shouldMove:
            if time.time() - lastTime >= 10:
                keyboard.release('w')  # Release the 'W' key if it was held for 10+ seconds
                print("W key released after 10+ seconds.")
                lastTime = time.time()  # Reset the lastTime variable to 0
                keyboard.press('w')
            else:
                print("Press")
                keyboard.press('w')
        else:
            print("No move")
            keyboard.release('w')  # Release the 'W' key if there's no movement
            lastTime = 0  # Reset the lastTime variable to 0

keyboard.release('w')