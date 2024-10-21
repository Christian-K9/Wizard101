import spell_index as si
import pyautogui as pya
import time

time.sleep(3)
pya.keyDown("A")
time.sleep(0.01)
pya.keyUp("A")
time.sleep(1)
pya.keyDown("W")
time.sleep(4)
pya.keyUp("W")
time.sleep(1)
pya.keyDown("D")
time.sleep(0.15)
pya.keyUp("D")
time.sleep(1)
pya.keyDown("W")
time.sleep(1.57)
pya.keyUp("W")
time.sleep(1.5)
pya.keyDown("X")
time.sleep(0.5)
pya.keyUp("X")
time.sleep(1)

si.spell_click(si.spell_maker("Go_In_Button"), 0, 0.7, False)