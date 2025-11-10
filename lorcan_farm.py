import pyautogui as pya
import spell_index as si
import time

def enter_dungeon():
    si.wait_for_image("Chamber_Symbol")
    si.print_cool_way("Entering Dungeon")
    pya.keyDown("X")
    time.sleep(0.5)
    pya.keyUp("X")
    time.sleep(20)
    pya.keyDown("W")
    time.sleep(5)
    pya.keyUp("W")

def cast_spell(spell):
    spell = si.spell_maker(spell)
    si.spell_click(spell, 0, 0.7, True)

def draw_card():
    print("Drawing Card")
    draw_button = si.spell_maker("Draw_Button")
    si.spell_click(draw_button, 0, 0.7, False)

def check_if_dead():
    si.print_cool_way("Checking If Enemy Is Dead...")
    Pass_Button = si.spell_maker("Pass_Button")
    dead = False
    Spell_Book = si.spell_maker("Spell_Book")
    position = si.image_search(Pass_Button, 0.6)
    while position == None:
        #If the pass button shows, then they're alive, if the spellbook shows, they're dead
        position = si.image_search(Pass_Button, 0.6)
        if (position != None):
            dead = False
            break
        time.sleep(1)
        position = si.image_search(Spell_Book, 0.6)
        if (position != None):
            dead = True
            exit
        time.sleep(1)
    return dead

def exit_dungeon():
        pya.keyDown("a")
        time.sleep(0.6)
        pya.keyUp("a")
        time.sleep(1)
        pya.keyDown("w")
        time.sleep(3)
        pya.keyUp("w")
        time.sleep(10)
    
def battle():
    first_round = True

    enchantments = [
        ("Sharpened_Blade", "Myth_Blade"),
        ("Sharpened_Blade", "Spirit_Blade"),
        ("Colossal", "Orthrus"),
        ("Colossal", "Ninja_Pigs")
    ]

    cards = {"Sharpened_Blade_Enchanted_Myth_Blade",
             "Sharpened_Blade_Enchanted_Spirit_Blade",
             "Myth_Blade", "Spirit_Blade"}
    
    global temp
    global counter
    global total_counter
    total_counter = 0
    counter = 0
    temp = ""

    def card_counter(card):
        global temp
        global counter
        global total_counter
        if temp == card:
            counter += 1
            total_counter += 1
            print("Counter: " + str(counter))
        if counter == 5:
            alternate(card)
            return True
        elif total_counter == 30:
            alternate(card)
            return True
        else:
            temp = card
            return False

    def alternate(card):
        opposites = {"Myth_Blade": "Sharpened_Blade_Enchanted_Myth_Blade",
                     "Spirit_Blade": "Sharpened_Blade_Enchanted_Spirit_Blade"}
        cast = None
        for i in opposites:
            if card == i:
                cast = opposites[i]
            elif card == opposites[i]:
                cast = i
        cast_spell(cast)
        si.cast_on_yourself()

    while len(cards) > 0:
        for card in cards:
            for ench, base in enchantments:
                if si.check_for_card(ench) and si.check_for_card(base):
                    si.enchant_card(ench, base)
                    pair = (ench, base)
                    enchantments.remove(pair)
                    break
            if first_round == True:
                draw_card()
                cast_spell("Summon_Kit_10")
                first_round = False
                si.print_cool_way("Waiting For Next Round...")
                si.wait_for_image("Pass_Button")
            print("Checking For Card: ", card)
            if card_counter(card) == True:
                cards.remove(card)
                break
            if si.check_for_card(card) == True:
                cast_spell(card)
                cards.remove(card)
                if card != "Beserk":
                    si.cast_on_yourself()
                    si.print_cool_way("Waiting For Next Round...")
                    si.wait_for_image("Pass_Button")
                break
    cast_spell("Beserk")
    counter = 1
    while counter <= 1:
        si.wait_for_image("Pass_Button")
        counter = si.identifyEnemies()
    si.wait_for_image("Pass_Button")
    cast_spell("Colossal_Enchanted_Orthrus")
    if check_if_dead() == False:
        #si.pass_round()
        cast_spell("Colossal_Enchanted_Ninja_Pigs")
        si.cast_on_enemy()
    si.print_cool_way("Victory")
        
def collecting_orbs():
    si.print_cool_way("Collecting Orbs")
    pya.keyDown("w")
    time.sleep(1.5)
    pya.keyUp("w")
    time.sleep(1)
    pya.keyDown("s")
    time.sleep(2.5)
    pya.keyUp("s")
    time.sleep(1)
while True:
    attempt = 0
    times = []
    attempt += 1
    average = 0
    if len(times) != 0:
        for i in times:
            average += i
            average /= len(times)
            average = round(average, 2)
            si.print_cool_way("\033[33m" + "Average Time Is " + str(average) + " Minutes" + "\033[0m")
    si.print_cool_way("\033[33m" + "Attempt: " + str(attempt) + "\033[0m")
    timing = time.time()
    si.print_cool_way("Now Farming Lucan")
    si.game_click()
    enter_dungeon()
    si.wait_for_image("Pass_Button")
    battle()
    exit_dungeon()
    collecting_orbs()
    timing = time.time() - timing
    timing = (int(timing)) / 60.0 
    timing = round(timing, 2)
    si.print_cool_way( "\033[33m" + "Timing: " + str(timing) + " Minutes" + "\033[0m")
    times.append(timing)