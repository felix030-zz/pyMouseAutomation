import pyautogui, sys
import curses

# pyautogui.typewrite('Hello world!', interval=0.25)

import keyboard #Using module keyboard
while True:#making a loop
    try: #used try so that if user pressed other than the given key error will not be shown

        x, y = pyautogui.position()
        positionStr = 'X: ' + str(x).rjust(4) + ' Y: ' + str(y).rjust(4)
        print(positionStr, end='')
        print('\b' * len(positionStr), end='', flush=True)

        if keyboard.is_pressed('q'):#if key 'q' is pressed
            print('You Pressed A Key!')


            # break#finishing the loop
        else:
            pass
    except:
        break #if user pressed other than the given key the loop will break