import pyautogui
from time import sleep
n=input("Enter the number: ")
n_int=int(n)
sleep(3)
for i in range (1,n_int+1):
    for j in range(0,i):
        pyautogui.write("#")
    pyautogui.press("enter")






