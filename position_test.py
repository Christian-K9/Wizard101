import spell_index as si
import pyautogui as pya
import time
import keyboard as key

<<<<<<< HEAD
position = si.image_search(si.spell_maker("Yourself"), 0.7)
if position != None:
    x,y = position
    pya.moveTo(x - 100, y - 20, 0.5, pya.easeOutQuad)
    time.sleep(1)
    pya.click()
    time.sleep(1)
    if si.check_for_card("Yes_Button") == True:
        yes_button = si.spell_maker("Yes_Button")
        si.spell_click(yes_button, 0, 0.7, False)
=======

def check_beans_feint():
    time.sleep(1)
    beans = si.spell_maker("Balance_Symbol")
    position = si.image_search(beans, 0.6)
    if position != None:
        x,y = position
        pya.moveTo(x + 5, y + 30, 0.5, pya.easeOutQuad)
        feint = si.spell_maker("Beans_Feint")
        position = si.image_search(feint, 0.9)
        if position != None:
            return True
    return False

print(check_beans_feint())
>>>>>>> parent of 7d77e3e (BIG UPDATE)
