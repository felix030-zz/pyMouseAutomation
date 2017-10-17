import pyautogui, sys
import time

toTheleft = 34
print('Press Ctrl-C to quit.')
try:
    while True:
        # neutral
        pyautogui.moveTo(1233, 1029)
        pyautogui.click()


        pyautogui.moveTo(62-toTheleft, 429)
        pyautogui.click()
        pyautogui.click()
        pyautogui.moveTo(62, 429)
        pyautogui.click()
        pyautogui.click()
        print("click")


        pyautogui.moveTo(930-toTheleft, 440)
        pyautogui.click()
        pyautogui.click()
        pyautogui.moveTo(930, 440)
        pyautogui.click()
        pyautogui.click()
        print("click")


        pyautogui.moveTo(54-toTheleft, 979)
        pyautogui.click()
        pyautogui.click()
        pyautogui.moveTo(54, 979)
        pyautogui.click()
        pyautogui.click()
        print("click")


        pyautogui.moveTo(1003-toTheleft, 979)
        pyautogui.click()
        pyautogui.click()
        pyautogui.moveTo(1003, 979)
        pyautogui.click()
        pyautogui.click()
        print("click")



        time.sleep(3 * 60)
except KeyboardInterrupt:
    print('\n')