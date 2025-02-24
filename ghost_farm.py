import spell_index as si
import time
import pyautogui as pya
import random

def cast_spell(spell):
    si.spell_click(si.spell_maker(spell), 0, 0.7, True)

def wait_next_round():
    si.wait_for_image("Pass_Button")

def check_if_dead():
    si.print_cool_way("Checking If Enemy Is Dead...")
    Pass_Button = si.spell_maker("Pass_Button")
    Spell_Book = si.spell_maker("Spell_Book")
    position = si.image_search(Pass_Button, 0.6)
    while position == None:
        #If the pass button shows, then they're alive, if the spellbook shows, they're dead
        position = si.image_search(Pass_Button, 0.6)
        if (position != None):
            return False
        time.sleep(1)
        position = si.image_search(Spell_Book, 0.6)
        if (position != None):
            return True
        time.sleep(1)

def alternate_attack():
    color = si.color_maker("Red")
    si.print_cool_way(color + str("Enemy Still Isn't Dead"))
    default = "default"
    si.print_cool_way(default + str("Attempting Alternate Hit"))
    si.enchant_card("Epic", "Humongofrog")
    cast_spell("Epic_Enchanted_Humongofrog")
    si.wait_for_image("Spell_Book")
    
def cast_on_yourself():
    si.print_cool_way("Casting On Player...")
    player = si.spell_click(si.spell_maker("Yourself"), 0, 0.7, False)

def cast_on_enemy():
    si.print_cool_way("Casting On Enemy...")
    enemy = si.spell_click(si.spell_maker(""))


def try_to_enchant():
    enchantments = ["Myth_Blade", "Spirit_Blade"]
    for i in enchantments:
        if (si.check_for_card(i) == True) and (si.check_for_card("Sharpened_Blade") == True):
            si.enchant_card("Sharpened_Blade", i)
            enchantments.remove(i)
            try_to_enchant()

#alright lets do this

def navigate():
    si.wait_for_image("Chamber_Of_Darkness_Symbol")
    pya.press("X")
    time.sleep(15)
    pya.keyDown("W")
    time.sleep(7)
    pya.keyUp("W")
    si.wait_for_image("Pass_Button")

def ghost_battle():
    wait_next_round()
    buffs = {"Sharpened_Blade_Enchanted_Myth_Blade": True, 
            "Sharpened_Blade_Enchanted_Spirit_Blade": True,
            "Frenzy": False}

    while len(buffs) > 0:
        for i in buffs:
            try_to_enchant()
            if si.check_for_card(i) == True:
                cast_spell(i)
                if buffs[i] == True:
                    cast_on_yourself()
                wait_next_round()
                buffs.pop(i)
    cast_spell("Epic_Enchanted_Orthrus")
    if check_if_dead() == False:
        alternate_attack()

def restart_dungeon():
    transport = si.spell_maker("Transport")
    si.spell_click(transport)
    time.sleep(10)


ghost_battle()

