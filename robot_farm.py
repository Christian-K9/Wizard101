import pyautogui as pya
import spell_index as si
import keyboard
import time

def cast_spell(spell, entity):
    if entity == "Yourself":
        cast_on_self = True
    else:
        cast_on_self = False
    if si.check_for_card(spell):
        spell = si.spell_maker(spell)
        si.spell_click(spell, 0, 0.7, True)
    if cast_on_self:
        si.cast_on_yourself()

spells = {"Orthrus": "Extract_Golumn",
          "Drop_Bear_Fury": "Epic"}

def battle():
    si.game_click()
    si.aot_victory()
    pya.moveTo(200, 200, 1, pya.easeOutQuad)
    for i in spells:
        si.enchant_card(spells[i], i)
    cast_spell("Frenzy", None)
    si.wait_for_image("Pass_Button")
    si.check_for_fizzles("Frenzy", False)
    cast_spell("Extract_Golumn_Enchanted_Orthrus", None)
    si.check_if_dead(["Extract_Golumn_Enchanted_Orthrus"], None, None)

while True:
    battle()