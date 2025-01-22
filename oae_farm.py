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


if __name__ == "__main__":
    main()

def aot_run(use_Enchanted, enchanted_card, spell_card):
    aot.print_cool_way("\033[33m" + "Make Sure You Are Standing In Front Of Enemies")
    aot.print_cool_way("Getting Ready In 5...")
    time.sleep(1)
    i = 4
    while i > 0:
        print(str(i) + "...")
        i -= 1
        time.sleep(1)
    print("\033[0m")

    aot.game_click()
    aot.move()
    attempt = 0
    seconds = time.time()
    while True:
        attempt += 1
        time_passed = time.time()
        time_passed -= seconds
        time_passed /= 60
        aot.print_cool_way("Time Passed: " + str(int(time_passed)) + " Minutes")
        aot.print_cool_way("\033[33m" + "Attempt Number: " + str(attempt) + "\033[0m")
        aot.aot_Battle(use_Enchanted, enchanted_card, spell_card)
        aot.victory_Idle("aot_battle")
