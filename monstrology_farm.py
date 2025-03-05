import spell_index as si
import oae_farm as oae
import time

def print_card_list(card_list):
    counter = 0
    for card in card_list:
        counter += 1
        si.print_cool_way("         " + str(counter) + "." + card)


rank = int(input("What Rank Are The Enemies? "))
enchanted_card = input("What Kind of Extract Are You Using? ")

si.print_cool_way("Now Starting Monstrology Farm")
time.sleep(5)

def higher_rank_battles():
    enchanted_list = []
    spell_card_list = []
    spell_card_list = []
    enchanted_list = []

    spell_card_list.append("Orthrus")
    enchanted_list.append("Extract_Undead")
    spell_card_list.append("Myth_Blade")
    spell_card_list.append("Spirit_Blade")
    spell_card_list.append("Frenzy")
    enchanted_list.append("Sharpened_Blade")

    time.sleep(3)
    si.game_click()
    si.aot_victory()
    while True:
        si.four_round_battle(enchanted_list, spell_card_list, None, None, "aot_battle")

def lower_rank_battles():
    use_Enchanted = True
    spell_card = "Orthrus"
    buff = "Sharpened_Blade"

    si.print_cool_way("\033[33m" + "Now Using The Default Myth AOT Farm")
    time.sleep(3)
    si.print_cool_way("Default Enchanted Card: Epic")
    si.print_cool_way("Default Spell Used: Orthrus")

    si.game_click()
    si.aot_victory()
    while True:
        si.two_round_battle(buff, "Myth_Blade","Spirit_Blade", enchanted_card, spell_card)

if rank < 15:
    lower_rank_battles()
elif rank >= 15:
    higher_rank_battles()
    