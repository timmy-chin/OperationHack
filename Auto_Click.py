import pyautogui
import time
from Username_ListMaker import username_list

new_list = username_list

time.sleep(10)
for i in range(32):
    pyautogui.typewrite(username_list[i])
    time.sleep(0.1)
    pyautogui.press('tab')
    time.sleep(0.1)
    pyautogui.press('enter')
    time.sleep(0.1)
    new_list.pop(i)

for i in range(20):
    pyautogui.press('tab')

pyautogui.press('enter')
time.sleep(3)
pyautogui.typewrite("Hello, I'm sure some of you have already noticed, my account timmy_chin_ got hacked. So, if you receive a message from that account asking for a screenshot, please ignore it.")


