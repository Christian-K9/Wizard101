import time
import pyautogui as pya
import spell_index as farm

farm.wait_for_image("Mount_Olympus_Floor_Pattern")
pya.keyDown("w")
time.sleep(0.50)
pya.keyUp("w")
farm.spell_click(farm.spell_maker("More_Button"), 0, 0.6)
time.sleep(1)
farm.spell_click(farm.spell_maker("Done_Button"), 0, 0.6)
time.sleep(1)
pya.keyDown("a")
time.sleep(4.220)
pya.keyDown("w")
time.sleep(0.160)
pya.keyUp("a")
