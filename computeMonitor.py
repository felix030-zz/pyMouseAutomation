import pyautogui, sys
import time



toTheleft = 34
print('Press Ctrl-C to quit.')
try:
    while True:

        with open('monitor.txt') as f:
            lines = f.readlines()

            for i in range(0, len(lines)):
                line = lines[i]
                arr = line.split()
                if len(arr) == 4:
                    x = int(arr[1])
                    y = int(arr[3])
                    pyautogui.moveTo(x, y)
                    # print(x + " " + y)
                elif len(arr) == 5:
                    pyautogui.click()
                    # print("click")

        time.sleep(3 * 60)
except KeyboardInterrupt:
    print('\n')