import pyautogui, sys
import time
import keyboard
import os

os.remove('monitor.txt')
print('Press Ctrl-C to quit.')

recList = []
try:
    while True:
        x, y = pyautogui.position()
        positionStr = 'X: ' + str(x).rjust(4) + ' Y: ' + str(y).rjust(4)

        with open('monitor.txt', "a") as f:
            f.write(positionStr + "\n")
            print(positionStr + "\n")

            if keyboard.is_pressed('shift'):
                f.write("clicked " + positionStr + "\n")
                print("clicked " + positionStr + "\n")

            if keyboard.is_pressed('ctrl'):
                recorded = keyboard.record(until='esc')
                recList.append(recorded)
                # f.write("keys start " + "\n")
                # f.write("".join(recorded))
                # f.write("\n"+ "keys end ")


            time.sleep(1)




except KeyboardInterrupt:
    print('\n')