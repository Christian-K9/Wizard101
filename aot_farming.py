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
    while x <= 30:
        pya.move(-10, 0, 0.01)
        image_search(spell, 0.4)
        x += 1
    # Move Right
    x = 0
    while x <= 30:
        pya.move(10, 0, 0.01)
        position = image_search(spell, 0.6)
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
    print("Current Directory Of Spell: " + str(spell_path))
    if not os.path.exists(spell_path):
        print("\033[31m" + "Spell Not Found: " + spell_path + "\033[0m")
        print("Make Sure Images Are In 'Spell_Folder' Files")
        sys.exit()
    return spell_path


def spell_click(spell, attempt, threshold):
    position = image_search(spell, threshold)
    if position != [-1, -1] and position != None:
        x, y = position
        x += 20
        print("Spell Found")
        print("position: " + str(position))
        pya.moveTo(x, y, 1, pya.easeOutQuad)
        pya.click()
        pya.moveTo(x, y + 100, 1, pya.easeOutQuad)
    else:
        # After Third Attempt It Will Scroll To Find Spell
        if attempt == 3:
            print("Attempting To Use Mouse to Find Spell")
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


def Battle():
    if (use_Enchanted == True):
        enchanted_spell = (enchanted_card + "_Enchanted_" + spell_card)
        spell_click(spell_maker(enchanted_card), 0, 0.6)
        time.sleep(3)
        spell_click(spell_maker(spell_card), 0, 0.6)
        time.sleep(3)
        spell_click(spell_maker(enchanted_spell), 0, 0.6)
    else:
        spell_click(spell_maker(spell_card), 0, 0.6)
    
# After Battle Is Finished It Doesn't Stop Moving Until Another Battle Starts
def Battle_Idle():
    print("Waiting Until Battle Is Finished...")
    # The Spell_Book Symbol Won't Display While In Combat
    Spell_Book = (spell_maker("Spell_Book"))
    position = image_search(Spell_Book, 0.6)
    # Waits Until Earn Crowns Symbol Is Displayed
    while position == None:
        time.sleep(1)
        position = image_search(Spell_Book, 0.6)
    if position != None:
        print("\033[32m" + "VICTORY!!!" + "\033[0m")
        time.sleep(3)
        print("Getting Ready For Next Battle")
        movement_list = ["a", "d"]
        Pass_Button = (spell_maker("Pass_Button"))
        position = image_search(Pass_Button, 0.6)
        while position == None:
            movement = random.choice(movement_list)
            pya.keyDown(movement)
            time.sleep(0.5)
            pya.keyUp(movement)
            position = image_search(Pass_Button, 0.6)
        print("Next Battle Ready")
        
def move():
    time.sleep(0.1)
    pya.keyDown("w")
    time.sleep(3)
    pya.keyUp("w")
    time.sleep(7)

spell_card = input("\033[32m" + "Enter The Spell You're Using: \033[0m")
use_Enchanted = False

if (input("\033[32m" + "Use Enchanted? y/n: \033[0m" ) == "y"):
    use_Enchanted = True
    enchanted_card = input("\033[32m" +"Which Enchanted Card? : \033[0m")


print("\033[33m" + "Make Sure You Are Standing In Front Of Enemies")
time.sleep(1)
print("Getting Ready In 3...")
time.sleep(1)
print("2...")
time.sleep(1)
print("1..."  + '\033[0m')
time.sleep(1)

game_click()
move()

while True:
    Battle()
    Battle_Idle()
