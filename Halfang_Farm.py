import spell_index as si
import pyautogui as pya
import time

si.print_cool_way("Now Starting Halfang Farm")
time.sleep(5)
attempt = 0
while True:
    attempt += 1
    si.print_cool_way("Attempt: " + str(attempt))
    si.game_click()
    si.wait_for_image("Halfang_Symbol")
    pya.press("x")
    time.sleep(15)
    pya.keyDown("W")
    time.sleep(5)
    pya.keyUp("W")
    si.wait_for_image("Pass_Button")
    si.enchant_card("Epic", "Drop_Bear_Fury")
    si.spell_click(si.spell_maker("Epic_Enchanted_Drop_Bear_Fury"), 0, 0.7, True)
    si.wait_for_image("Spell_Book")
    si.print_cool_way("Victory")
    time.sleep(2)
    pya.keyDown("W")
    time.sleep(4)
    pya.keyUp("W")
    time.sleep(2)
