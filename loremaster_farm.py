import spell_index as farm
import time

enchanted_list = []
spell_card_list = []

spell_card_list.append(input("\033[32m" + "Which Hitter Are You're Using?: \033[0m"))
enchanted_list.append(input("Which Enchanted Card For The Hit?: "))
spell_card_list.append(input("What Is Your First Buff?: "))
spell_card_list.append(input("What Is Your Second Buff?: "))
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
print("1..."  + '\033[0m')
time.sleep(1)

farm.game_click()
farm.move()

while True:
    farm.three_round_battle(enchanted_list, spell_card_list)
