
import spell_index as farm
import time
import pyautogui as pya


enchanted_list = []
spell_card_list = []

spell_card_list.append(input("\033[32m" + "Which Hitter Are You're Using?: " + "\033[0m"))
enchanted_list.append(input("\033[32m" + "Which Enchanted Card For The Hit?: " + "\033[0m"))
spell_card_list.append(input("\033[32m" + "What Is Your First Buff?: " + "\033[0m"))
spell_card_list.append(input("\033[32m" + "What Is Your Second Buff?: " + "\033[0m"))
spell_card_list.append(input("\033[32m" + "What Is Your Third Buff?" + "\033[0m"))
enchanted_list.append("Sharpened_Blade")

print("\033[33m" + "Make Sure You Are Standing In Front Of Enemies")
time.sleep(1)
print("Getting Ready In 5...")
time.sleep(1)
print("4...")
time.sleep(1)
print("3...")
time.sleep(1)
print("2...")
time.sleep(1)
print("1..." + "\033[0m")
time.sleep(1)

while True:
    farm.game_click()
    farm.enter_dungeon()
    farm.move()
    farm.three_round_battle(enchanted_list, spell_card_list)
    pya.keyDown("s")
    time.sleep(0.5)
    pya.keyUp("s")