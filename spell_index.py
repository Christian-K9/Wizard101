import pyautogui as pya
import cv2
import sys
import numpy as np
from pyautogui import *
import os
import keyboard
from PIL import Image
import imagesearch as img
import time
import random

def exit_game():
    sys.exit()

keyboard.add_hotkey('q', exit_game)

def print_cool_way(sentence):
    for i in sentence:
        if i == "_":
            i = " "
        print(i, end="", flush=True)
        time.sleep(0.05)
    print()

def print_cool_way1(sentence, threshold):
    for i in sentence:
        if i == "_":
            i = " "
        print(i, end="", flush=True)
        time.sleep(threshold)
    print()
# Function to search for an image on the screen
def image_search(image_path, theshold):
    screen = pya.screenshot()
    screen_np = np.array(screen)
    screen_gray = cv2.cvtColor(screen_np, cv2.COLOR_RGB2GRAY)

    template = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
    w, h = template.shape[::-1]

    result = cv2.matchTemplate(screen_gray, template, cv2.TM_CCOEFF_NORMED)
    loc = np.where(result >= theshold)

    if loc[0].size > 0:
        x = loc[1][0] + w // 2
        y = loc[0][0] + h // 2
        return (x, y)
    else:
        return None

#\033[0m – Reset (default color)
#\033[30m – Black
#\033[31m – Red
#\033[32m – Green
#\033[33m – Yellow
#\033[34m – Blue
#\033[35m – Magenta
#\033[36m – Cyan
#\033[37m – White
def color_maker(color):
    colors = ["Black", "Red", "Green", "Yellow", "Blue", "Magenta", "Cyan", "White"]
    index = 0
    while index < len(colors):
        if color == "default":
            return "\033[0m"
        elif color == colors[index]:
            return "\033[3" + str(index) + "m"
        index += 1
# Scroll across screen if image isn't found
def scroll_and_search(spell):
    spell_found = False
    position = None
    x = 0
    print_cool_way1("Moving Mouse Left", 0.03)
    while x <= 50:
        pya.move(-25, 0, 0.01)
        position = image_search(spell, 0.4)
        if position != [-1, -1] and position != None:
            x, y = position
            x -= 10
            print("Spell Found")
            print("position: " + str(position))
            pya.moveTo(x, y, 1, pya.easeOutQuad)
            pya.click()
            pya.moveTo(x, y + 100, 1, pya.easeOutQuad)
            spell_found = True
            return spell_found
        x += 1

    print_cool_way1("Moving Mouse Right", 0.03)
    x = 0
    while x <= 50:
        if spell_found == True:
            return spell_found
        pya.move(25, 0, 0.01)
        position = image_search(spell, 0.4)
        if position != [-1, -1] and position != None:
            x, y = position
            x -= 10
            print("Spell Found")
            print("position: " + str(position))
            pya.moveTo(x, y, 1, pya.easeOutQuad)
            pya.click()
            pya.moveTo(x, y + 100, 1, pya.easeOutQuad)
        x += 1
    if position == [-1, -1]:
        print("\033[31m" + str(spell) + " Not Found On Screen")
        print("Exiting" + "\033[0m]")
        sys.exit()


def spell_maker(spell):
    current_dir = os.getcwd()
    spell = spell + ".png"
    spell_path = os.path.join(current_dir, "Spell_Folder", spell)
    if not os.path.exists(spell_path):
        print("\033[31m" + "Image Not Not Found: " + spell_path + "\033[0m")
        print("Make Sure Images Are In 'Spell_Folder' Files")
        sys.exit()
    return spell_path


def spell_click(spell, attempt, threshold, cast):
    if cast == True:
      new_spell = "Wizard101\\Spell_Folder\\"
      position = spell.find(new_spell)
      spell_casting = spell[position + len(new_spell):]
      spell_casting = spell_casting[0:len(spell_casting) - 4]
      
      if position != -1:  # If the spell is found in the string
        print_cool_way("Attempting To Cast " + str(spell_casting) + "...")

    position = image_search(spell, threshold)
    if position != [-1, -1] and position != None:
        x, y = position
        pya.moveTo(x, y, 0.5, pya.easeOutQuad)
        pya.click()
        pya.moveTo(x, y + 100, 0.5, pya.easeOutQuad)
    else:
        # After Third Attempt It Will Scroll To Find Spell
        if attempt == 3:
            print_cool_way("\033[33m" + "Attempting To Use Mouse to Find Spell..." + "\033[0m")
            scroll_and_search(spell)
            exit
        else:
            print_cool_way1("\033[31m" + "Spell Not Found" + "\033[0m", 0.03)
            print_cool_way1("Attempting To Find Spell Again...", 0.03)
            attempt += 1
            
            spell_click(spell, attempt, threshold, cast)

def discard_card(spell):
    position = image_search(spell_maker(spell), 0.6)
    if position != None:
        x, y = position
        pya.moveTo(x, y, 0.5, pya.easeOutQuad)
        pya.click(button="right")
        time.sleep(1)
        pya.moveTo(x, y - 100, 0.5, pya.easeOutQuad)

def game_click():
    position = image_search(spell_maker("Spell_Book"), 0.7)
    if position != None:
        x, y = position
        x = int(x) - 500
        y = int(y) - 500
        pya.moveTo(x, y, 0.5, pya.easeOutQuad)
        pya.click()
        time.sleep(0.5)
        pya.moveTo(x, y - 100, 0.5, pya.easeOutQuad)
    #middle = 1393 477
    #spell book = 1837, 817

def enchant_card(enchanted, spell):
    print_cool_way1("Attempting To Enchant " + str(enchanted) + " With " + str(spell) + "...", 0.03)
    spell_click(spell_maker(enchanted), 0, 0.6, False)
    time.sleep(0.5)
    spell_click(spell_maker(spell), 0, 0.6, False)
    time.sleep(0.5)

def cast_on_yourself():
    spell_click(spell_maker("Yourself"), 0, 0.8, False)
    
def identifyEnemies():
    counter = 0
    enemies = ["dagger", "key", "gem", "spiral"]
    for i in enemies:
        position = image_search(spell_maker(i), 0.8)
        if position != None:
            counter += 1
    if counter == 1:
        print_cool_way("There Is " + str(counter) + " Enemy In Battle")
    else:
        print_cool_way("There Are " + str(counter) + " Enemies In Battle")
    return counter

def pass_round():
    position = image_search(spell_maker("Pass_Button"), 0.6)
    if position != None:
        spell_click(spell_maker("Pass_Button"), 0, 0.6, False)

def aot_Battle(use_Enchanted, enchanted_card, spell_card):
    enemies = identifyEnemies()
    while enemies < 2:
        print_cool_way("\033[31m" + "Not All Enemies Have Joined" + "\033[0m")
        print_cool_way("Waiting For Next Round...")
        pass_round()
        wait_for_image("Pass_Button")
        enemies = identifyEnemies()
    pya.moveTo(200, 200, 0.5, pya.easeOutQuad)
    if (use_Enchanted == True):
        enchanted_spell = (enchanted_card + "_Enchanted_" + spell_card)
        enchant_card(enchanted_card, spell_card)
        spell_click(spell_maker(enchanted_spell), 0, 0.6, True)
    else:
        spell_click(spell_maker(spell_card), 0, 0.6)
    check_if_dead([enchanted_card], None, None)


def two_round_battle(buff_enchant, buff,spell_enchant, spell):
    pya.moveTo(200, 200, 0.5, pya.easeOutQuad)
    enchant_card(buff_enchant, buff)
    enchant_card(spell_enchant, spell)

    buff = buff_enchant + "_Enchanted_" + buff
    hitter = spell_enchant + "_Enchanted_" + spell
    spell_click(spell_maker(buff), 0, 0.7, True)
    cast_on_yourself()
    battle_idle()
    check_for_fizzles(buff, True)
    spell_click(spell_maker(hitter), 0, 0.7, True)
    check_if_dead([hitter], None, None)
    victory_Idle("aot_battle")

def three_round_battle(buff_enchant, first_buff, second_buff,spell_enchant, spell):
    pya.moveTo(200, 200, 0.5, pya.easeOutQuad)
    enchant_card(buff_enchant, first_buff)
    enchant_card(buff_enchant, second_buff)
    enchant_card(spell_enchant, spell)

    first_buff = buff_enchant + "_Enchanted_" + first_buff
    second_buff = buff_enchant + "_Enchanted_" + second_buff
    hitter = spell_enchant + "_Enchanted_" + spell
    spell_click(spell_maker(first_buff), 0, 0.7, True)
    cast_on_yourself()
    battle_idle()
    check_for_fizzles(first_buff, True)
    spell_click(spell_maker(second_buff), 0, 0.7, True)
    cast_on_yourself
    battle_idle()
    victory_Idle("aot_battle")


#Blades You Twice, Then Cast Orthrus  
def four_round_battle(enchanted_list, spell_card_list, alternate_buff, alternate_hitter, battle_type):
    identifyEnemies()
    #enchanted_list[0] = enchant for buff
    #enchanted_list[1] = enchant for spell
    #spell_card_list[0] = first buff
    #spell_card_list[1] = second buff
    #spell_card_list[2] = hit
    #spell_card_list[3] = third buff

    pya.moveTo(200, 200, 0.5, pya.easeOutQuad)

    enchant_card(enchanted_list[0], spell_card_list[0])
    enchant_card(enchanted_list[1], spell_card_list[1])
    enchant_card(enchanted_list[1], spell_card_list[2])

    enchanted_spell_list = []
    enchanted_spell_list.append((enchanted_list[1] + "_Enchanted_" + spell_card_list[1]))
    enchanted_spell_list.append((enchanted_list[1] + "_Enchanted_" + spell_card_list[2]))
    enchanted_spell_list.append(spell_card_list[3])
    enchanted_spell_list.append((enchanted_list[0] + "_Enchanted_" + spell_card_list[0]))

    print()

    i = 0
    while i < 4:
        cast_on_player = False
        spell_click(spell_maker(enchanted_spell_list[i]), 0, 0.7, True)
        if i < 2:
            cast_on_yourself()
            cast_on_player = True
        if i == 3:
            break
        battle_idle()
        check_for_fizzles(enchanted_spell_list[i], cast_on_player,)
        i += 1
    time.sleep(2)
    check_if_dead(enchanted_spell_list, alternate_buff, alternate_hitter)
    victory_Idle(battle_type)
        
def cast_on_enemy():
    print_cool_way("Casting Spell On Enemy...")
    enemies = ["dagger", "key", "gem", "spiral"]
    for i in enemies:
        enemy = spell_maker(i)
        position = image_search(enemy, 0.6)
        if position != None:
            spell_click(enemy, 0, 0.6, False)

def alternate_attempt(alternate_buff, alternate_hitter):
    alternate_list = [alternate_buff, alternate_hitter]
    print_cool_way("Attempting Alternate Hit")
    Draw_Button = spell_maker("Draw_Button")
    position = image_search(Draw_Button, 0.6)
    if position != None:
        spell_click(Draw_Button, 0, 0.6, False)
        i = 0
        #Clicks the draw button until the buff shows up
        while i < 2:
            if check_for_card(alternate_list[i]) == False:
                print_cool_way("Drawing Card...")
                spell_click(Draw_Button, 0, 0.6, False)
                time.sleep(1)
            else:
                spell_click(spell_maker(alternate_list[i]), 0, 0.7, True)
                if i == 0:
                    cast_on_yourself()
                    battle_idle()
                    check_for_fizzles(alternate_list[i], True)
                else:
                    cast_on_enemy()
                    time.sleep(1)
                    exit
                i += 1
        check_if_dead(None, alternate_buff, alternate_hitter)
    

def Flee_Battle():
    print_cool_way("\033[31m" + "Forced To Flee Battle" + "\033[0m")
    Flee_Button = spell_maker("Flee_Button")
    spell_click(Flee_Button, 0, 0.6)
    Yes_Button = spell_maker("Yes_Button")
    spell_click(Yes_Button, 0, 0.6)

def check_for_card(spell):
    spell = spell_maker(spell)
    position = image_search(spell, 0.7)
    if position == None:
        return False
    elif position != None:
        return True


def check_if_dead(enchanted_spell_list, alternate_buff, alternate_hitter):
    print_cool_way("Checking If Enemy Is Dead...")
    Pass_Button = spell_maker("Pass_Button")
    dead = False
    Spell_Book = spell_maker("Spell_Book")
    position = image_search(Pass_Button, 0.6)
    while position == None:
        #If the pass button shows, then they're alive, if the spellbook shows, they're dead
        position = image_search(Pass_Button, 0.6)
        if (position != None):
            dead = False
            break
        time.sleep(1)
        position = image_search(Spell_Book, 0.6)
        if (position != None):
            dead = True
            exit
        time.sleep(1)

    # If They are dead and the spell the last spell is still in the deck
    if ((no_more_cards(enchanted_spell_list) == False) and (dead == False)):
        print("\033[31m" + "Something During Battle Occured..." + "\033[0m")
        print_cool_way("Attempting To Cast Spell Again...")
        spell_click(spell_maker(enchanted_spell_list[-1]), 0, 0.6, True)
        check_if_dead(enchanted_spell_list, alternate_buff, alternate_hitter)

    # If they're not dead and theres buffs and hitters in the alternates loaded
    elif (dead == False)  and (no_more_cards(enchanted_spell_list) == True):
        print_cool_way("\033[31m" + "Enemy Still Isn't Dead" + "\033[0m")
        alternate_attempt(alternate_buff, alternate_hitter)

    # If they're not dead and theres no more cards in the deck
    elif (dead == False) and (no_more_cards(enchanted_spell_list) == True):
        print_cool_way("\033[31m" + "Enemy Still Isn't Dead" + "\033[0m")
        Flee_Battle()
    
def wait_for_image(image):
    spell = spell_maker(image)
    position = image_search(spell, 0.7)
    while position == None:
        time.sleep(0.5)
        position = image_search(spell, 0.7)

def no_more_cards(enchanted_spell_list):
    if enchanted_spell_list == None:
        return False
    else:
        position = image_search(spell_maker(enchanted_spell_list[-1]), 0.6)
        if position == None:
            return True
        else:
            return False

def check_for_fizzles(last_spell_used, cast_on_player):
        time.sleep(1)
        print_cool_way("Checking For Fizzles...")
        spell = spell_maker(last_spell_used)
        position = image_search(spell, 0.6)
        if position == None:
            exit
        elif position != None:
            print_cool_way("\033[31m" + "Something During Battle Occured..." + "\033[0m")
            print_cool_way("Attempting To Cast Spell Again...")
            spell_click(spell, 0, 0.7, True)
            if cast_on_player == True:
                cast_on_yourself()
            battle_idle()
            check_for_fizzles(last_spell_used, cast_on_player)

def battle_idle():
    print_cool_way("Waiting For Next Round...")
    wait_for_image("Pass_Button")

def aot_victory():
        position = image_search(spell_maker("Pass_Button"), 0.6)
        while position == None:
            if check_for_card("Pass_Button") == True:
                break
            pya.keyDown("w")
            time.sleep(1.5)
            pya.keyUp("w")
            if check_for_card("Pass_Button") == True:
                break
            time.sleep(0.5)
            pya.keyDown("s")
            time.sleep(1.5)
            pya.keyUp("s")
            position = image_search(spell_maker("Pass_Button"), 0.6)

# After Battle Is Finished It Doesn't Stop Moving Until Another Battle Starts
def victory_Idle(battle_type):
    print_cool_way("\033[32m" + "VICTORY!!!" + "\033[0m")
    time.sleep(3)
    print_cool_way("Getting Ready For Next Battle...")
    game_click()
    if (battle_type == "aot_battle"):
        aot_victory()

    elif (battle_type == "dungeon_battle"):
            exit_loremaster_dungeon()
        
def move():
    time.sleep(0.1)
    pya.keyDown("w")
    time.sleep(3)
    pya.keyUp("w")
    battle_idle()
    
def turn_around():
    pya.keyDown("a")
    time.sleep(0.27)
    pya.keyUp("a")

def enter_dungeon(spell):
    game_click()
    pya.keyDown("x")
    time.sleep(0.95)
    pya.keyUp("x")
    print_cool_way("Waiting To Enter Dungeon...")
    wait_for_image(spell)

def exit_loremaster_dungeon():
    print_cool_way("Exiting Dungeon...")
    turn_around()
    turn_around()
    pya.keyDown("w")
    time.sleep(4)
    pya.keyUp("w")
    print_cool_way("Waiting...")
    wait_for_image("Dragonspyre_Floor_Pattern")
