import loremaster_farm as farm
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
alternate_hitter = ("Otomo_Fury_Treasure_Card")

print("\033[33m" + "Default Spells Used: ")
print("Spell Card List " + str(spell_card_list))
print("Enchanted Spell List " + str(enchanted_list))
print("Alternate Buff: " + alternate_buff)
print("Alternate Hitter: " + alternate_hitter)

print("\033[33m" + "Make Sure You Are Standing In Front Of The Sigil")
time.sleep(1)
print("Getting Ready In 10...")
i = 9
while i > 0:
    print(str(i) + "...")
    i -= 1
    time.sleep(1)
print("\033[0m")

farm.loremaster_run(enchanted_list, spell_card_list, alternate_buff, alternate_hitter)