import pyautogui as pya
import spell_index as si
import time

def cast_spell(spell, wait_image):
    yourself = False
    if spell == "Item_Myth_Blade":
        yourself = True
    if si.check_for_card(spell):
        spell = si.spell_maker(spell)
        si.spell_click(spell, 0, 0.7, True)
        if yourself == True:
            si.cast_on_yourself()
        si.print_cool_way("Waiting Next Round...")
        si.wait_for_image(wait_image)

def battle():
    pya.moveTo(200, 200, 1, pya.easeOutQuad)
    si.enchant_card("Extract_Golumn", "Orthrus")
    si.enchant_card("Epic", "Drop_Bear_Fury")
    cast_spell("Frenzy", "Pass_Button")
    cast_spell("Item_Myth_Blade", "Pass_Button")
    cast_spell("Extract_Golumn_Enchanted_Orhtrus", "Spell_Book")

si.print_cool_way("Now Starting Stray Cat Farm..")
si.print_cool_way("Starting in...")
i = 5
while i > 0:
    si.print_cool_way(str(i) + "...")
    i -= 1
    time.sleep(1)

attempt = 0
times = []
average = 0

while True:
    if len(times) != 0:
        for i in times:
            average += i
    average /= len(times)
            #average = round(average, 2)
    si.print_cool_way("\033[33m" + "Average Time Is " + str(average) + " Minutes" + "\033[0m")
    attempt += 1
    si.print_cool_way("Attempt: " + str(attempt))
    timing = time.time()
    si.game_click()
    si.aot_victory()
    battle()
    timing = time.time() - timing
    timing = (int(timing)) / 60.0
    #timing = round(timing, 2)
    si.print_cool_way( "\033[33m" + "Timing: " + str(timing) + " Minutes" + "\033[0m")
    times.append(timing)