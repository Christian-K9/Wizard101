import os
import sys
import time
import spell_index as si
import os
import sys
import threading
import time
import keyboard  # Install with: pip install keyboard

def enchant_card(enchanted, spell):
    si.print_cool_way1("Attempting To Enchant " + str(enchanted) + " With " + str(spell) + "...", 0.03)
    si.spell_click(si.spell_maker(enchanted), 0, 0.9, False)
    time.sleep(0.5)
    si.spell_click(si.spell_maker(spell), 0, 0.9, False)
    time.sleep(0.5)


def try_to_enchant():
    enchanted_list = {"Orthrus": "Colossal",
                      "Myth_Blade": "Sharpened_Blade",
                      "Spirit_Blade": "Sharpened_Blade",
                      "Feint": "Potent_Trap"}
    for i in enchanted_list:
        spell = si.spell_maker(i)
        enchantment = si.spell_maker(enchanted_list[i])
        if (si.image_search(spell, 0.9) != None) and (si.image_search(enchantment, 0.9) != None):
            enchant_card(enchanted_list[i], i)
            try_again = True
    try_again = False
    if try_again == True:
        try_to_enchant()


try_to_enchant()