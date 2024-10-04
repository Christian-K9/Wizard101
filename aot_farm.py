import spell_index as aot
import pyautogui as pya
import time

def move():
    pya.keyDown("w")
    
def main():
    spell_card = input("\033[32m" + "Enter The Spell You're Using: \033[0m")
    use_Enchanted = False

    if (input("\033[32m" + "Use Enchanted? y/n: \033[0m" ) == "y"):
        use_Enchanted = True
        enchanted_card = input("\033[32m" +"Which Enchanted Card? : \033[0m")

    aot_run(use_Enchanted, enchanted_card, spell_card)


print("\033[33m" + "Make Sure You Are Standing In Front Of Enemies")
print("Getting Ready In 10...")
i = 9
while i > 0:
    print(str(i) + "...")
    i -= 1
    time.sleep(1)
print("\033[0m")

aot.game_click()
aot.move()

if __name__ == "__main__":
    main()

def aot_run(use_Enchanted, enchanted_card, spell_card):
    while True:
        aot.aot_Battle(use_Enchanted, enchanted_card, spell_card)
        aot.victory_Idle("aot_battle")
