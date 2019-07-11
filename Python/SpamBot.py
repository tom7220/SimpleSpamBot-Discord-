#Simple spambot made by tom7220
#This spam bot was designed for discord. In full screen mode.
#If you add a delay it will bypass the "chill zone in discord"

import pyautogui
#(x=789, y=985)
print(pyautogui.position())

while True:
    pyautogui.click(789, 985)
    pyautogui.typewrite("@James120#2742 ")
    pyautogui.typewrite(["enter"])
    print("Sending spam")
