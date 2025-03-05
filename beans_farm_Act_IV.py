import pyautogui as pya
import spell_index as si
import time

def cast_spell(spell, entity):
    spell = si.spell_maker(spell)
    si.spell_click(spell, 0, 0.7, True)
    entities = {"quizzler": "Myth_Symbol", "player": "Yourself",
                "beans": "Life_Symbol", "pork": "Fire_Symbol",
                "sparck": "Balance_Symbol", "medulla": "Myth_Symbol"}
    for i in entities:
        if i == entity:
            si.spell_click(entities[i], 0, 0.7, False)

def wait_next_round():
    si.wait_for_image("Pass_Button")

def check_if_dead():
    spell_book = si.spell_maker("spell_book")
    pass_button = si.spell_maker("pass_button")

    while True:
        if si.check_for_card(spell_book) == True:
            return True
        elif si.check_for_card(pass_button) == True:
            return False
        time.sleep(0.5)

#Collect Orbs
def collect_orbs():
    si.print_cool_way("Collecting Orbs...")
    pya.keyDown("s")
    time.sleep(7)
    pya.keyUp("s")
    time.sleep(1)
    pya.keyDown("w")
    time.sleep(7)
    pya.keyUp("w")
    time.sleep(1)
    if si.check_for_card("Headquarters_Symbol") == True:
        return
    else:
        si.spell_click(si.spell_maker("Pinpoint"), 0, 0.9, False)

#Enter Dungeon
def enter_dungeon():
    dungeon = si.spell_maker("Headquarters_Symbol")
    if si.check_for_card(dungeon) == True:
        pya.press("x")
        time.sleep(15)

#Navigate Through First Half Dungeon

#Quizzler Battle
def quizzler_battle():
    cast_spell("Myth_Prism", "quizzler")
    wait_next_round()
    si.enchant_card("Epic", "Orhtrus")
    orthrus = "Epic_Enchanted_Orthrus"
    cast_spell(orthrus, None)
    if check_if_dead() == False:
        si.spell_click("Pass_Button", 0, 0.7, False)
        humongofrog = "Epic_Enchanted_Humongofrog"
        cast_spell(humongofrog, None)
    si.wait_for_image("Spell_Book")

#Navigate Through Second Half of Dungeon

reshuffle = 4
#Medulla Fight
def final_fight():
    def try_to_discard(spells):
        global reshuffle
        for i in spells:
            if si.check_for_card(i) != True:
                if (i == "reshuffle") and (reshuffle > 1):
                    print(True)
                    reshuffle -= 1
                    print("Reshuffles Left: " + str(reshuffle))
                si.discard_card(i)
    
    def try_to_enchant(part):
        if part == 1:
            spells = {"Celestial_Calendar": "Epic", "Ninja_Piga": "Epic"}
        elif part == 2:
            spells = {"Potent_Trap": "Feint"}
        for i in spells:
            if (si.check_for_card(i) == True) and (si.check_for_card(spells[i]) == True):
                si.enchant_card(spells, spells[i])

    def free_friend(friend):
        try_to_enchant(1)
        try_to_discard["Potent_Trap", "Frenzy", "Reshuffle", "Myth_Prism"]
        position = si.image_search(friend, 0.9)
        while position != None:
            cast_spell("Clear_Mind", friend)
            wait_next_round()


    #Free Pork and Sparck 
    def part_one():
        if si.check_for_card("Frenzy") == True:
            cast_spell("Frenzy", None)
        elif si.check_for_card("Feint") == True:
            cast_spell("Feint", "beans")
        else:
            pass_button = si.spell_maker("Pass_Button")
            si.spell_click(pass_button, 0, 0.7, False)
        wait_next_round()
        pork = "Fire_Symbol"
        free_friend(pork)
        sparck = "Balance_Symbol"
        free_friend(sparck)

#   Find Beans (Four Methods)
    def find_beans_ver_I(cast):
        beans = "Life_Symbol"
        position = si.image_search(beans, 0.9)
        if position != None:
            x,y = position
            pya.moveTo(x + 30, y + 5, 0.5, pya.easeOutQuad)
            time.sleep(1)
            pya.click()
        else:
            return False
        
    def find_beans_ver_II(cast):
        beans = "Beans_Name"
        position = si.image_search(beans, 0.9)
        if position != None:
            x,y = position
            pya.moveTo(x, y, 0.5, pya.easeOutQuad)
            time.sleep(1)
            pya.click()
        else:
            return False
        
    def find_beans_ver_III(cast):
        beans = "Life_Symbol_Ver_II"
        position = si.image_search(beans, 0.9)
        if position != None:
            x,y = position
            pya.moveTo(x + 30, y + 5, 0.5, pya.easeOutQuad)
            time.sleep(1)
            pya.click()
        else:
            return False
        
    def find_beans_ver_IV(cast):
        medulla = si.spell_maker("Myth_Symbol")
        enemies = ["dagger", "key", "gem", "spiral"]
        alive_enemies = []
        for i in enemies:
            enemy = si.spell_maker(i)
            if si.image_search(enemy, 0.7) != None:
                alive_enemies.append(enemy)
        if len(alive_enemies) > 0:
            if len(alive_enemies) != 2:
                return False
            elif len(alive_enemies) == 2:
                medulla_pos = si.image_search(medulla, 0.7)
                first_pos = si.image_search(alive_enemies[0], 0.7)
                second_pos = si.image_search(alive_enemies[1], 0.7)
                if (first_pos != None) and (second_pos != None):
                    x_one, y_one = first_pos
                    x_two, y_two = second_pos
                    x_medulla, y_medulla = medulla_pos
                    x_one -= x_medulla
                    x_two -= x_medulla
                    if abs(x_one > x_two):
                        print("Beans is: " + alive_enemies[0])
                        pya.moveTo(x_one + 30, y_one, 0.5, pya.easeOutQuad)
                        pya.click()

                    elif abs(x_two > x_one):
                        print("Beans is: " + alive_enemies[1])
                        pya.moveTo(x_two + 30, y_two, 0.5, pya.easeOutQuad)
                        pya.click()
        else:
            return False
        
    def find_beans_ver_V(alive_enemy):
        enemies = ["dagger", "key", "gem", "spiral"]
        alive_enemies = []
        for i in enemies:
            enemy = si.spell_maker(i)
            position = si.image_search(enemy, 0.8)
            if position != None and (enemy != alive_enemy):
                x, y = position
                pya.moveTo(x + 35, y, 0.5, pya.easeOutQuad)
                time.sleep(1)
                pya.click()
                return True
    
    def find_beans():
        methods = [find_beans_ver_I, find_beans_ver_II,
                   find_beans_ver_III, find_beans_ver_IV,
                   find_beans_ver_V]
        
        for i in methods:
            if i() != False:
                return
            else:
                return True
        False

#   Fight Beans
    def part_two():
        while si.check_for_card("Feint") == False:
            try_to_discard["Reshuffle", "Frenzy", "Myth_Prism", "Potent_Trap", "Clear_Mind"]
            try_to_enchant(1)
        if si.check_for_card("Beans_Shield") == True:
            pass_button = si.spell_maker("Pass_Button")
            si.spell_click(pass_button, 0, 0.7, False)
            wait_next_round()
        cast_spell("Feint", None)
        find_beans()
        wait_next_round()
        while find_beans() == False:
            print()

#   Fight Medulla
#   Exit Dungeon