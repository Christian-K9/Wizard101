import loremaster_farm as farm
import spell_index as si
import time

spell_card_list = []
enchanted_list = []

spell_card_list.append("Orthrus")
enchanted_list.append("Epic")
spell_card_list.append("Myth_Blade")
spell_card_list.append("Spirit_Blade")
spell_card_list.append("Frenzy")
enchanted_list.append("Sharpened_Blade")
alternate_buff = ("Myth_Blade_Treasure_Card")
alternate_hitter = ("Stone_Colossus_Treasure_Card")

def print_card_list(card_list):
    counter = 0
    for card in card_list:
        counter += 1
        si.print_cool_way("         " + str(counter) + "." + card)

si.print_cool_way("\033[33m" + "Now Using Default Myth Loremaster Farm...")
print()
time.sleep(3)
si.print_cool_way("Default Spells Used: ")
si.print_cool_way("     Spell Card List: ")
print_card_list(spell_card_list)
time.sleep(3)
si.print_cool_way("     Enchanted Spell List:")
print_card_list(spell_card_list)
time.sleep(3)
si.print_cool_way("     Alternate Buff: " + alternate_buff)
si.print_cool_way("     Alternate Hitter: " + alternate_hitter)
print()
time.sleep(5)

si.print_cool_way("\033[33m" + "Make Sure You Are Standing In Front Of The Sigil")
time.sleep(1)
si.print_cool_way("Getting Ready In 10...")
time.sleep(1)
i = 9
while i > 0:
    print(str(i))
    i -= 1
    time.sleep(1)
print("\033[0m")

farm.loremaster_run(enchanted_list, spell_card_list, alternate_buff, alternate_hitter)