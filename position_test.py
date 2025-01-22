import spell_index as si
import pyautogui as pya
import time
import keyboard as key


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