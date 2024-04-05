import pyautogui
from time import *
sleep(4)
for i in range(0,3):
    pyautogui.write('Hello world! ', interval=0.25)
