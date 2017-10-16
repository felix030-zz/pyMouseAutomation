import pyautogui, sys

print('Press Ctrl-C to quit.')
try:
    while True:
        pyautogui.moveTo(100, 200)
        pyautogui.moveRel(0, 50)
        pyautogui.moveRel(-30, 0)
        pyautogui.moveRel(-30, None)
except KeyboardInterrupt:
    print('\n')