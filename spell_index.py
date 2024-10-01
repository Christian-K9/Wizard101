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

# Function to search for an image on the screen
def image_search(image_path, theshold):
    screen = pya.screenshot()
    screen_np = np.array(screen)
    screen_gray = cv2.cvtColor(screen_np, cv2.COLOR_RGB2GRAY)

    # Load the target image
    template = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
    w, h = template.shape[::-1]

    # Perform template matching
    result = cv2.matchTemplate(screen_gray, template, cv2.TM_CCOEFF_NORMED)
    loc = np.where(result >= theshold)  # Adjust the threshold as necessary

    if loc[0].size > 0:
        # Get the center point of the found image
        x = loc[1][0] + w // 2
        y = loc[0][0] + h // 2
        return (x, y)  # Return the center coordinates
    else:
        return None  # Image not found

# Scroll across screen if image isn't found


def scroll_and_search(spell):
    position = None
    x = 0
    # Move Left
    while x <= 50:
        pya.move(-10, 0, 0.01)
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
    # Move Right
    x = 0
    while x <= 50:
        pya.move(10, 0, 0.01)
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
    print("Current Directory: " + str(current_dir))
    spell = spell + ".png"
    print("Attempting To Find " + spell)
    spell_path = os.path.join(current_dir, "Spell_Folder", spell)
    print("Current Directory Of Image: " + str(spell_path))
    if not os.path.exists(spell_path):
        print("\033[31m" + "Image Not Not Found: " + spell_path + "\033[0m")
        print("Make Sure Images Are In 'Spell_Folder' Files")
        sys.exit()
    return spell_path


def spell_click(spell, attempt, threshold):
    position = image_search(spell, threshold)
    if position != [-1, -1] and position != None:
        x, y = position
        x -= 10
        print(str(spell) + " Found")
        print("position: " + str(position))
        pya.moveTo(x, y, 0.5, pya.easeOutQuad)
        pya.click()
        pya.moveTo(x, y + 100, 0.5, pya.easeOutQuad)
    else:
        # After Third Attempt It Will Scroll To Find Spell
        if attempt == 3:
            print("Attempting To Use Mouse to Find Spell...")
            scroll_and_search(spell)
        else:
            attempt += 1
            spell_click(spell, attempt, threshold)

def game_click():
    position = image_search(spell_maker("Spell_Book"), 0.6)
    if position != None:
        x, y = position
        x = int(x) - 500
        y = int(y) - 500
        pya.moveTo(x, y, 1, pya.easeOutQuad)
        pya.click()
        time.sleep(1)
    #middle = 1393 477
    #spell book = 1837, 817

def pass_round():
    spell_click(spell_maker("Pass_Button"))

def enchant_card(enchanted, spell):
    print("Attempting To Enchant " + str(enchanted) + " With " + str(spell) + "...")
    spell_click(spell_maker(enchanted), 0, 0.6)
    time.sleep(0.5)
    spell_click(spell_maker(spell), 0, 0.6)
    time.sleep(0.5)

def cast_on_yourself():
    spell_click(spell_maker("Yourself"), 0, 0.8)
    
def aot_Battle(use_Enchanted, enchanted_card, spell_card):
    if (use_Enchanted == True):
        enchanted_spell = (enchanted_card + "_Enchanted_" + spell_card)
        enchant_card(enchanted_card, spell_card)
        spell_click(spell_maker(enchanted_spell), 0, 0.6)
    else:
        spell_click(spell_maker(spell_card), 0, 0.6)

#Blades You Twice, Then Cast Orthrus  
def four_round_battle(enchanted_list, spell_card_list):
    #enchanted_list[0] = enchant for buff
    #enchanted_list[1] = enchant for spell
    #spell_card_list[0] = first buff
    #spell_card_list[1] = second buff
    #spell_card_list[2] = hit
    #spell_card_list[3] = third buff
    enchant_card(enchanted_list[0], spell_card_list[0])
    enchant_card(enchanted_list[1], spell_card_list[1])
    enchant_card(enchanted_list[1], spell_card_list[2])

    enchanted_spell_list = []
    enchanted_spell_list.append((enchanted_list[1] + "_Enchanted_" + spell_card_list[1]))
    enchanted_spell_list.append((enchanted_list[1] + "_Enchanted_" + spell_card_list[2]))
    enchanted_spell_list.append(spell_card_list[3])
    enchanted_spell_list.append((enchanted_list[0] + "_Enchanted_" + spell_card_list[0]))

    print("Order Of Spells: " + str(enchanted_spell_list))
    i = 0
    while i < 4:
        spell_click(spell_maker(enchanted_spell_list[i]), 0, 0.7)
        if i < 2:
            cast_on_yourself()
        if i == 3:
            break
        battle_idle()
        check_for_fizzles(enchanted_spell_list[i])
        i += 1
    victory_Idle("dungeon_battle", enchanted_spell_list[-1])
        
def wait_for_image(image):
    spell = spell_maker(image)
    position = image_search(spell, 0.6)
    # Waits Until Pass Button Is Displayed
    while position == None:
        time.sleep(0.5)
        position = image_search(spell, 0.6)

def next_round(last_spell_used):
    wait_for_image("Pass_Button")
    position = image_search(spell_maker(last_spell_used), 0.6)
    if position != None:
        print("Something During Battle Occured")
        print("Attempting To Cast Spell Again")
        spell_click(spell_maker(last_spell_used), 0, 0.7)


def check_for_fizzles(last_spell_used):
        time.sleep(1)
        position = image_search(spell_maker("Pass_Button"), 0.6)
        if position != None:
            next_round(last_spell_used)

def battle_idle():
    print("Waiting For Battle To Start...")
    wait_for_image("Pass_Button")

# After Battle Is Finished It Doesn't Stop Moving Until Another Battle Starts
def victory_Idle(battle_type, last_spell_used):
    print("Waiting Until Battle Is Finished...")
    # The Spell_Book Symbol Won't Display While In Combat
    Spell_Book = (spell_maker("Spell_Book"))
    Pass_Button = (spell_maker("Pass_Button"))
    position = image_search(Spell_Book, 0.6)
    while position == None:
        check_for_fizzles(last_spell_used)
        time.sleep(1)
        position = image_search(Spell_Book, 0.6)
        time.sleep(1)
    if position != None:
        print("\033[32m" + "VICTORY!!!" + "\033[0m")
        time.sleep(3)
        print("Getting Ready For Next Battle...")
        if (battle_type == "aot_battle"):
            movement_list = ["a", "d"]
            position = image_search(Pass_Button, 0.6)
            while position == None:
                movement = random.choice(movement_list)
                pya.keyDown(movement)
                time.sleep(0.5)
                pya.keyUp(movement)
                position = image_search(Pass_Button, 0.6)
        elif (battle_type == "dungeon_battle"):
            turn_around()
            exit_dungeon()
            time.sleep(7)
    print("Next Battle Ready")
        
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

def enter_dungeon():
    game_click()
    pya.keyDown("x")
    time.sleep(0.95)
    pya.keyUp("x")
    print("Waiting To Enter Dungeon")
    time.sleep(20)

def exit_dungeon():
    print("Exiting Dungeon...")
    turn_around()
    pya.keyDown("w")
    time.sleep(4)
    pya.keyUp("w")
    print("Waiting...")
    time.sleep(10)