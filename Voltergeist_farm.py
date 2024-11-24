
import spell_index as farm
import time
import pyautogui as pya
import keyboard


def main():
    enchanted_list = []
    spell_card_list = []

    spell_card_list.append(input("\033[32m" + "Which Hitter Are You're Using?: " + "\033[0m"))
    enchanted_list.append(input("\033[32m" + "Which Enchanted Card For The Hit?: " + "\033[0m"))
    spell_card_list.append(input("\033[32m" + "What Is Your First Buff?: " + "\033[0m"))
    spell_card_list.append(input("\033[32m" + "What Is Your Second Buff?: " + "\033[0m"))
    spell_card_list.append(input("\033[32m" + "What Is Your Third Buff?: " + "\033[0m"))
    alternate_buff = input("\033[32m" + "(Optional) Do You Want To Add An Alternate Buff?: " + "\033[0m")
    alternate_hitter = input("\033[32m" + "(Optional) Do You Want To Add An Alternate Hitter?: " + "\033[0m")
    enchanted_list.append("Sharpened_Blade")

    print("\033[33m" + "Make Sure You Are Standing In Front Of The Sigil")
    time.sleep(1)
    print("Getting Ready In 10...")
    i = 9
    while i > 0:
        print(str(i) + "...")
        i -= 1
    time.sleep(1)
    print("\033[0m")

    voltergeist_run(enchanted_list, spell_card_list, alternate_buff, alternate_hitter)

def voltergeist_run(enchanted_list, spell_card_list, alternate_buff, alternate_hitter):
    attempt = 0
    while True:
        attempt += 1
        farm.print_cool_way("Waiting For Spell Book")
        farm.wait_for_image("Spell_Book")
        farm.print_cool_way("\033[33m" + "Attempt Number: " + str(attempt) + "\033[0m")
        farm.game_click()
        farm.enter_dungeon("Voltergeist_Wall_Pattern")
        farm.move()
        farm.four_round_battle(enchanted_list, spell_card_list, alternate_buff, alternate_hitter, "dungeon_battle")
        pya.keyDown("s")
        time.sleep(0.5)
        pya.keyUp("s")

if __name__ == "__main__":
    main()

    