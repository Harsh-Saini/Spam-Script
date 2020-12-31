import pyautogui, time
time.sleep(5)
b = 0
while b < 200:
    a = open('spam.txt','r')
    for w in a:
        pyautogui.typewrite(w)
        pyautogui.press('enter')
        b += 1
        time.sleep(2)