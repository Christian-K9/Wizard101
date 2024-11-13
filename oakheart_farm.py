import spell_index as si
import pyautogui as pya
import keyboard as key
import time

time.sleep(5)
si.print_cool_way("Attempting To Enter Dungeon...")
si.game_click()
key.press("x")

while True:
    time.sleep(5)
    pya.keyDown("x")
    time.sleep(0.5)
    pya.keyUp("x")
    while (si.check_for_card("Oakhearts_Lair_Symbol") == True) :
        si.print_cool_way("Something Occured")
        si.print_cool_way("Attempting To Enter Dungeon Again")
        pya.keyDown("x")
        time.sleep(0.5)
        pya.keyUp("x")
        time.sleep(2)
    si.wait_for_image("Oakheart_Done_Button")
    time.sleep(2)
    si.spell_click(si.spell_maker("Oakheart_Done_Button"), 0, 0.7, False)
    time.sleep(2)
    pya.keyDown("w")
    time.sleep(2)
    pya.keyUp("w")
    si.battle_idle()
    si.enchant_card("Epic", "Drop_Bear_Fury")
    si.spell_click(si.spell_maker("Epic_Enchanted_Drop_Bear_Fury"), 0, 0.7, True)
    si.wait_for_image("Spell_Book")
    si.print_cool_way("\033[32m" + "VICTORY!!!" + "\033[0m")
    time.sleep(2)
    pya.keyDown("a")
    time.sleep(0.65)
    pya.keyUp("a")
    time.sleep(1)
    pya.keyDown("w")
    time.sleep(3)
    pya.keyUp("w")
    spell = si.spell_maker("Oakheart_Tree_Pattern")
    position = si.image_search(spell, 0.7)
    while position == None:
        time.sleep(0.5)
        position = si.image_search(spell, 0.7)
        if position != None:
            break
        spell = si.spell_maker("Oakhearts_Lair_Symbol")
        position = si.image_search(spell, 0.7)
        if position != None:
            break
        spell = si.spell_maker("Oakheart_Tree_Pattern")
        time.sleep(0.5)

    pya.keyDown("s")
    time.sleep(1.5)
    pya.keyUp("s")
