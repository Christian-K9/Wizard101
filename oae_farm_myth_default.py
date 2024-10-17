import oae_farm as aot
import spell_index as si
import time

use_Enchanted = True
enchanted_card = "Epic"
spell_card = "Drop_Bear_Fury"

si.print_cool_way("\033[33m" + "Now Using The Default Myth AOT Farm")
time.sleep(3)
si.print_cool_way("Default Enchanted Card: Epic")
si.print_cool_way("Default Spell Used: Drop Bear Fury")
aot.aot_run(use_Enchanted, enchanted_card, spell_card)