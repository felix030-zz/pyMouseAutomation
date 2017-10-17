import pyautogui, sys
import curses
import keyboard #Using module keyboard

# pyautogui.typewrite('Hello world!', interval=0.25)

def writeToFile(aString):
    with open('log.txt', "a") as f:
        f.write(aString)

def checkForStringInFile(aString):
    with open('log.txt', 'a') as f:
        lines = f.readlines()

        for i in range(0, len(lines)):
            line = lines[i]
            if positionStr in line:
                print("String was aready added")
                # return True
            else:
                print("String was not added yet")
                # writeToFile(aString)
                # return False

while True:
    try: #used try so that if user pressed other than the given key error will not be shown

        if keyboard.is_pressed('q'):#if key 'q' is pressed
            x, y = pyautogui.position()
            positionStr = 'X: ' + str(x).rjust(4) + ' Y: ' + str(y).rjust(4)

            # if checkForStringInFile(positionStr) == True:
            #     print("Writing value")
            checkForStringInFile(positionStr)

            print(positionStr, end='')
            print('\b' * len(positionStr), end='', flush=True)



            # if check == False:
            #     with open('log.txt', 'a') as f:
            #         f.write(positionStr)

            # break#finishing the loop
        else:
            pass
    except:
        break #if user pressed other than the given key the loop will break





