import spell_index as aot
import time

spell_card = input("\033[32m" + "Enter The Spell You're Using: \033[0m")
use_Enchanted = False

if (input("\033[32m" + "Use Enchanted? y/n: \033[0m" ) == "y"):
    use_Enchanted = True
    enchanted_card = input("\033[32m" +"Which Enchanted Card? : \033[0m")


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

aot.game_click()
aot.move()

while True:
    aot.Battle(use_Enchanted, enchanted_card, spell_card)
    aot.Battle_Idle()
