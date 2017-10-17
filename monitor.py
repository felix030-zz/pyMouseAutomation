import pyautogui, sys
import time
import keyboard

print('Press Ctrl-C to quit.')
try:
    while True:
        x, y = pyautogui.position()
        positionStr = 'X: ' + str(x).rjust(4) + ' Y: ' + str(y).rjust(4)

        with open('monitor.txt', "a") as f:
            f.write(positionStr + "\n")

            if keyboard.is_pressed('shift'):
                f.write("clicked " + positionStr + "\n")

            time.sleep(1)




except KeyboardInterrupt:
    print('\n')