import time
import pyautogui as pya
import threading as td
import spell_index as si
import keyboard
import sys

started_battle = False
timeout = False

def travel_to_gladiator():
    global started_battle
    started_battle = False
    si.wait_for_image('Mount_Olympus_Floor_Pattern')
    si.game_click()
    pya.click()
    pya.keyDown('W')
    time.sleep(5.01)
    pya.keyUp('W')
    time.sleep(0.5)
    pya.keyDown('D')
    time.sleep(0.53)
    pya.keyUp('D')
    time.sleep(0.5)
    pya.keyDown('W')
    time.sleep(3.92)
    pya.keyUp('W')
    time.sleep(1)
    pya.keyDown('A')
    time.sleep(0.53)
    pya.keyUp('A')
    pya.click()
    time.sleep(1)
    time.sleep(0.5)
    pya.keyDown('W')
    time.sleep(9.4)
    pya.keyUp('W')
    time.sleep(0.5)
    pya.keyDown('A')
    time.sleep(0.658)
    pya.keyUp('A')
    pya.click()
    time.sleep(1)
    pya.keyDown('W')
    time.sleep(3.65)
    pya.keyUp('W')
    time.sleep(1)
    pya.keyDown('A')
    time.sleep(0.377)
    pya.keyUp('A')
    pya.click()
    time.sleep(1)
    time.sleep(0.528)
    pya.keyDown('W')
    time.sleep(9)
    pya.keyUp('W')
    pya.keyDown("W")
    time.sleep(10)
    pya.keyUp("W")
    while started_battle == False:
        started_battle = si.check_for_card("Pass_Button")
        if timeout == True:
            return

def counter():
    global timeout
    timeout = False
    global started_battle
    si.print_cool_way("\033[33m" + "Player Has One Minute To Enter Battle" "\033[0m")
    count = 60
    while count > 0:
        if started_battle == True:
            print("\033[32m" + "Player Has Started Battle With Gladiator" + "\033[0m")
            print("Stopping Timer...")
            return
        print(count)
        time.sleep(1)
        count -= 1
    if count == 0:
        started_battle = False
        timeout = True

def quit():
    while True:
        if keyboard.is_pressed("q"):
            sys.exit()

def travel_through_dungeon():
    t1 = td.Thread(target = travel_to_gladiator)
    t2 = td.Thread(target = counter)

    t1.start()
    t2.start()

    t1.join()
    t2.join()

    if (timeout == True) and (started_battle == False) and (si.check_for_card("Dungeon_Leave_Sign")):
        si.print_cool_way("\033[31m" + "THIS DOESN'T MAKE ANY SENSE" + "\033[0m")
        time.sleep(2)
        si.print_cool_way("\033[31m" + "WHY ARE THE MOVEMENTS SO RANDOM?!?!?!?!?" + "\033[0m")
        time.sleep(2)
        si.print_cool_way("\033[31m" + "KINGSISLE HAS TO BE DOING THIS ON PURPOSE!!!" + "\033[0m")
        time.sleep(2)
        si.print_cool_way("Anyways Now I'm Transfering Back To Aquilla")
        time.sleep(1)
        si.spell_click(si.spell_maker("Dungeon_Yes_Button"), 0, 0.7, False)
        time.sleep(5)
        transport_back()
        si.wait_for_image("Garden_Pattern")
        victory_idle()
        si.game_click()
        pya.click()
        pya.keyDown("X")
        time.sleep(0.5)
        pya.keyUp("X")
        position = si.image_search(si.spell_maker("Go_In_Button"), 0.7)
        if position != None:
            si.spell_click(si.spell_maker("Go_In_Button"), 0, 0.7, False)
        time.sleep(1)
        si.print_cool_way("Waiting To Enter Dungeon...")
        si.wait_for_image('Mount_Olympus_Floor_Pattern')
        travel_through_dungeon()

    elif started_battle == False:
        pya.keyUp("W")
        si.print_cool_way("\033[31m" + "Battle Didn't Start" + "\033[0m")
        si.print_cool_way("Restarting Dungeon...")
        transport_back()
        si.wait_for_image("Garden_Pattern")
        victory_idle()
        si.game_click()
        pya.click()
        pya.keyDown("X")
        time.sleep(0.5)
        pya.keyUp("X")
        position = si.image_search(si.spell_maker("Go_In_Button"), 0.7)
        if position != None:
            si.spell_click(si.spell_maker("Go_In_Button"), 0, 0.7, False)
        time.sleep(1)
        si.print_cool_way("Waiting To Enter Dungeon...")
        si.wait_for_image('Mount_Olympus_Floor_Pattern')
        travel_through_dungeon()

        

# Priority of Spells:
#   1. cleanse charm (if there is a negative on player)
#   2. shatter (if gladiator has protection) 
#   3. wand myth blade, portent trap enchanted feint, feint
#   4. epic enchanted orthrus


# Order of Actions:
#   1. discard reshuffle (if found in hand)
#   2. enchant feint/potent trap and orthrus/epic (if both are found in hand)
#   3. cast all buffs needed
#   4. cast orthrus


def cast_on_gladiator():
    gladiator = si.spell_maker("Balance_Symbol")
    if si.image_search(gladiator, 0.9) != None:
        position = si.image_search(gladiator, 0.9)
        x, y = position
        pya.moveTo(x + 25, y - 5, 0.5, pya.easeOutQuad)
        pya.click()

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

def check_for_reshuffle(attempt):
    if (attempt == 1) and (si.check_for_card("reshuffle") == True):
        si.discard_card("reshuffle")

def check_enemy_stats():
    si.print_cool_way("Checking Enemy Stats...")
    gladiator = si.spell_maker("Balance_Symbol")
    if si.image_search(gladiator, 0.9) != None:
        position = si.image_search(gladiator, 0.9)
        x, y = position
        pya.moveTo(x + 25, y - 5, 0.5, pya.easeOutQuad)

def check_player_stats():
    print("Checking Player Stats")
    position = si.image_search(si.spell_maker("Yourself"), 0.8)
    if position != None:
        x, y = position
        x = int(x)
        y = int(y)
        pya.moveTo(x, y, 0.5, pya.easeOutQuad)

def check_for_negatives(last_round):
    check_player_stats()
    if (si.check_for_card("Gladiator_Negative_Blade") == True) and (si.check_for_card("Draw_Button") == True):
        Cleanse_Charm = si.check_for_card("Cleanse_Charm")
        attempt = 0
        while Cleanse_Charm == False:
            if attempt == 3:
                si.discard_card("Shatter")
            draw_button = si.spell_maker("Draw_Button")
            si.spell_click(draw_button, 0, 0.6, False)
            time.sleep(1)
            Cleanse_Charm = si.check_for_card("Cleanse_Charm")
            attempt += 1
        si.spell_click(si.spell_maker("Cleanse_Charm"), 0, 0.6, True)
        si.cast_on_yourself()
        si.battle_idle()
        check_for_negatives(last_round)
    elif (si.check_for_card("Gladiator_Negative_Blade") == True) and (si.check_for_card("Draw_Button") == False):
        si.discard_card("Shatter")
        si.battle_idle()
        check_for_fizzles("Cleanse_Charm", True, False)
        check_for_negatives(last_round)
        if last_round == True:
            check_for_protections(last_round)
    
def check_for_protections(last_round):
    check_enemy_stats()
    protection = si.check_for_card("Gladiator_Protections")
    legion_shield = si.check_for_card("Gladiator_Legion_Shield")
    tower_shield = si.check_for_card("Gladiator_Tower_Shield")
    if (protection or legion_shield or tower_shield) and (si.check_for_card("Draw_Button") == True):
        si.spell_click(si.spell_maker("shatter"), 0, 0.6, True)
        cast_on_gladiator()
        si.battle_idle()
        check_for_protections(last_round)
        check_for_negatives(last_round)

def check_for_fizzles(last_spell_used, cast_on_player, cast_on_enemy):
        time.sleep(1)
        si.print_cool_way("Checking For Fizzles...")
        spell = si.spell_maker(last_spell_used)
        position = si.image_search(spell, 0.6)
        if position == None:
            exit
        elif position != None:
            si.print_cool_way("\033[31m" + "Something During Battle Occured..." + "\033[0m")
            si.print_cool_way("Attempting To Cast Spell Again...")
            si.spell_click(spell, 0, 0.7, True)
            if cast_on_player == True:
                si.cast_on_yourself()
            elif cast_on_enemy == True:
                cast_on_gladiator()
            si.battle_idle()
            check_for_fizzles(last_spell_used, cast_on_player, cast_on_enemy)

def reshuffle():
    unready = si.check_for_card("Unready_Reshuffle")
    while unready == True:
        "\033[31m" + "Player Doesn't Have Enough Pips" + "\033[0m"
        si.spell_click(si.spell_maker("Pass_Button"), 0, 0.7, False)
        si.battle_idle()
        unready = si.check_for_card("Unready_Reshuffle")
    si.spell_click(si.spell_maker("reshuffle"), 0, 0.7, True)
    si.cast_on_yourself()
    si.battle_idle()

def check_reshuffled_deck():
    spells = ["Wand_Myth_Blade", "Spirit_Blade", "Epic", "Feint", "Potent_Trap"]
    si.battle_idle()
    for i in spells:
        if si.check_for_card(i) == True:
            return True
    return False

def check_if_dead(attempt):
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


    if (dead == False) and (si.check_for_card("Epic_Enchanted_Orthrus") == True):
        si.print_cool_way("\033[31m" + "Something During Battle Occured..." + "\033[0m")
        si.print_cool_way("Attempting To Cast Spell Again...")
        si.spell_click(si.spell_maker("Epic_Enchanted_Orthrus"), 0, 0.7, True)
        time.sleep(2)
        check_if_dead(attempt)
    
    elif (dead == False) and (si.check_for_card("Epic_Enchanted_Orthrus") == False) and (si.check_for_card("reshuffle") == True):
        si.print_cool_way("\033[31m" + "Enemy Still Isn't Dead" + "\033[0m")
        si.print_cool_way("Reshuffling Deck...")
        reshuffle()
        while check_for_reshuffle == False:
            reshuffle()
            check_reshuffled_deck()
        gladiator_battle(attempt + 1)

    elif (dead == False) and (si.check_for_card("Epic_Enchanted_Orthrus") == False) and (si.check_for_card("reshuffle") == False):
        si.print_cool_way("\033[31m" + "Enemy Still Isn't Dead" + "\033[0m")
        si.print_cool_way("\033[31m" + "Reshuffle Isn't Found" + "\033[0m")
        si.print_cool_way("Passing Round")
        si.spell_click(si.spell_maker("Pass_Button"), 0, 0.7, False)
        si.battle_idle()
        if si.check_for_card("reshuffle") == True:
            reshuffle()
            while check_for_reshuffle == False:
                reshuffle()
                check_reshuffled_deck()
            gladiator_battle(attempt + 1)
        else:
            si.Flee_Battle()
            sys.exit()

def transport_back():
    si.print_cool_way("Transporting Back To Aquilla")
    position = si.image_search(si.spell_maker("Transport"), 0.8)
    if position != None:
        si.spell_click(si.spell_maker("Transport"), 0, 0.7, False)

def victory_idle():
    si.game_click()
    time.sleep(1)
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
    time.sleep(3)
    pya.keyDown("W")
    time.sleep(1.5)
    pya.keyUp("W")
    time.sleep(3)
    if si.check_for_card("Mount_Olympus_Enter_Symbol") == False:
        si.print_cool_way("\033[31m" + "Player Didn't Make It To Sigil" + "\033[0m")
        time.sleep(1)
        si.print_cool_way("Attempting To Go To Sigil Again...")
        time.sleep(1)
        si.print_cool_way("Waiting For Transport Timer To Reset...")
        i = 12
        while i > 0:
            print(i)
            time.sleep(1)
            i -= 1
        transport_back()
        victory_idle()

def gladiator_battle(attempt):
    buffs = ["Sharpened_Blade_Enchanted_Myth_Blade", "Potent_Trap_Enchanted_Feint", "Sharpened_Blade_Enchanted_Spirit_Blade", "Wand_Feint"]

    si.identifyEnemies()
    check_for_reshuffle(attempt)

    while(len(buffs) > 0):
        for i in buffs:
            try_to_enchant()
            check_for_negatives(False)
            spells = si.spell_maker(i)
            cast_on_player = False
            cast_on_enemy = False
            position = si.image_search(spells, 0.9)
            if position != None:
                si.spell_click(spells, 0, 0.9, True)
                if i == "Sharpened_Blade_Enchanted_Myth_Blade" or i == "Sharpened_Blade_Enchanted_Spirit_Blade":
                    si.cast_on_yourself()
                    cast_on_player = True
                else:
                    cast_on_gladiator()
                    cast_on_enemy = True

                si.battle_idle()
                check_for_fizzles(i, cast_on_player, cast_on_enemy)
                buffs.remove(i)
                si.battle_idle()
                break
            elif (position == None) and (i == buffs[-1]):
                position = si.image_search(si.spell_maker("Pass_Button"), 0.7)
                if position != None:
                    si.print_cool_way("Passing Round")
                    si.spell_click(si.spell_maker("Pass_Button"), 0, 0.7, False)
                    si.battle_idle()

    
    check_for_negatives(False)
    check_for_protections(False)

    time.sleep(2)
    unready = si.check_for_card("Unready_Orthrus")
    while unready == True:
        si.print_cool_way("\033[31m" + "Player Doesn't Have Enough Pips" + "\033[0m")
        si.spell_click(si.spell_maker("Pass_Button"), 0, 0.7, False)
        si.battle_idle()
        time.sleep(2)
        unready = si.check_for_card("Unready_Orthrus")
    
    si.print_cool_way("Final Check...")
    check_for_negatives(True)
    check_for_protections(True)


    si.spell_click(si.spell_maker("Epic_Enchanted_Orthrus"), 0, 0.6, True)
    check_if_dead(attempt)


def main():
    default_buffs = ["Wand_Attached_Myth_Blade", "Sharpened_Enchanted_Spirit_Blade", "Potent_Enchanted_Spirit_Blade"]
    default_hit = "Orthrus"
    additional_spells = ["Reshuffle", "Shatter", "Cleanse_Charm_Treasure_Card"]

    si.print_cool_way("\033[33m" + "Now Using The Gladiator Farm")
    time.sleep(1)
    print()
    #si.print_cool_way("Press 'q' To Quit Anytime")
    #time.sleep(1)
    #print()

    si.print_cool_way("Default Buffs Used:")
    counter = 0
    for i in default_buffs:
        counter += 1
        si.print_cool_way("     " + str(counter) + "." + i)

    print()
    si.print_cool_way("Default Hit:")
    si.print_cool_way("     " + default_hit)

    print()
    si.print_cool_way("Additional Spells Used:")
    counter = 0
    for i in additional_spells:
        counter += 1
        si.print_cool_way("     " + str(counter) + "." + i)

    print()
    si.print_cool_way("Make Sure You Are Standing In Front Of Dungeon")
    print()

    si.print_cool_way("Starting Farm in 5...")
    time.sleep(1)
    i = 4
    while i > 0:
        print(i)
        time.sleep(1)
        i -= 1
    print("\033[0m")

    attempt = 0
    times = []
    while True:
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
        si.game_click()
        pya.click()
        pya.keyDown("X")
        time.sleep(0.5)
        pya.keyUp("X")
        time.sleep(2 )
        position = si.image_search(si.spell_maker("Go_In_Button"), 0.7)
        if position != None:
            si.spell_click(si.spell_maker("Go_In_Button"), 0, 0.7, False)
        si.print_cool_way("Waiting To Enter Dungeon...")
        si.wait_for_image('Mount_Olympus_Floor_Pattern')
        travel_through_dungeon()
        si.wait_for_image("Pass_Button")
        gladiator_battle(1)
        si.print_cool_way("\033[32m" + "VICTORY!!!" + "\033[0m")
        si.print_cool_way("Getting Ready For Next Battle...")
        transport_back()
        si.wait_for_image("Garden_Pattern")
        victory_idle()
        timing = time.time() - timing
        timing = (int(timing)) / 60.0 
        timing = round(timing, 2)
        si.print_cool_way( "\033[33m" + "Timing: " + str(timing) + " Minutes" + "\033[0m")
        times.append(timing)

main()