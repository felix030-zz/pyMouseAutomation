import pyautogui, sys
import time



print('Press Ctrl-C to quit.')
try:
    while True:
        pyautogui.click()
        print("clicked")
        # time.sleep(1)
except KeyboardInterrupt:
    print('\n')