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
            enemy = si.spell_maker(entities[i])
            position = si.image_search(enemy, 0.6)
            x, y = position
            pya.moveTo(x + 25, y - 5, 0.5, pya.easeOutQuad)
            pya.click()

def cast_on_beans(spell):
        click = si.spell_maker(spell)
        si.spell_click(click, 0, 0.7, True)
        if find_beans_1(True) == True:
            return
        elif find_beans_2(True) == True:
            return
        elif find_beans_3() == True:
            return
        else:
            final_measure(spell)

def find_beans_1(click):
    beans = si.spell_maker("Beans_Name")
    position = si.image_search(beans, 0.9)
    if position != None:
        if click == True:
            si.spell_click(beans, 0, 0.7, 0)
        return True
    else:
        return False
    
def find_beans_2(click):
    beans = si.spell_maker("Life_Symbol")
    position = si.image_search(beans, 0.9)
    if position != None:
        if click == True:
            x,y = position
            pya.moveTo(x + 30, y + 5, 0.5, pya.easeOutQuad)
            time.sleep(1)
            pya.click()
    else:
        return False


def find_beans_3():
    medulla = si.spell_maker("Myth_Symbol")
    enemies = ["dagger", "key", "gem", "spiral"]
    alive_enemies = []
    for i in enemies:
        enemy = si.spell_maker(i)
        if si.image_search(enemy, 0.7) != None:
            alive_enemies.append(enemy)
    if len(alive_enemies) > 0:
        beans_finding = find_beans_4(alive_enemies[0])
        if len(alive_enemies) != 2 and beans_finding == None:
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



    
def find_beans_4(alive_enemy):
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

def final_measure(spell):
    time.sleep(1)
    medulla = si.spell_maker("Myth_Symbol")
    position = si.image_search(medulla, 0.7)
    if position != None:

        x_pos,y_pos = position
        x_points = [182, 437, 678, 924]
        difference = 1023
        coordinate = 0
        for x in x_points:
            temp = max(x_pos, x) - min(x_pos, x)
            if temp < difference:
                difference = temp
                coordinate = x

        for x in x_points:
            if x != coordinate:
                si.spell_click(spell, 0, 0.7, False)
                pya.moveTo(x, 82, 0.25, pya.easeOutQuad)
                pya.click()
                time.sleep(1)


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
round_number = 0
enchanted = False
#Medulla Fight
def final_fight():
    def try_to_discard(spells):
        global reshuffle
        for i in spells:
            if si.check_for_card(i) == True:
                if (i == "Reshuffle") and (reshuffle > 1):
                    print(True)
                    reshuffle -= 1
                    print("Reshuffles Left: " + str(reshuffle))
                si.discard_card(i)
    
    def try_to_enchant(part):
        if part == 1:
            spells = {"Witch's_House_Call" : "Extract_Pig", "Celestial_Calendar": "Extract_Pig", "Ninja_Pigs": "Extract_Pig"}
        elif part == 2:
            spells = {"Feint": "Potent_Trap"}
        for i in spells:
            if (si.check_for_card(i) == True) and (si.check_for_card(spells[i]) == True):
                si.enchant_card(spells[i], i)
                
    def free_friend(friend):
        global round_number
        si.print_cool_way("Attempting To Free Friend")
        try_to_enchant(1)
        friends = {"pork": "Fire_Symbol",
                   "sparck": "Balance_Symbol"}
        try_to_discard(["Potent_Trap", "Frenzy", "Reshuffle", "Myth_Prism"])
        for i in friends:
            if i == friend:
                entity = si.spell_maker(friends[i])
        while si.image_search(entity, 0.7) != None:
            si.print_cool_way("Attempting to free " + friend)
            round_number += 1
            cast_spell("Clear_Mind", friend)
            wait_next_round()


    #Free Pork and Sparck 
    def part_one():
        try_to_enchant(1)
        try_to_enchant(2)
        global enchanted
        feint = "Feint"
        enchanted_feint = "Potent_Trap_Enchanted_Feint"
        if si.check_for_card(enchanted_feint) == True:
            cast_on_beans(enchanted_feint)
            enchanted = True
        elif si.check_for_card(feint) == True:
            cast_on_beans(feint)
        else:
            try_to_discard(["Reshuffle"])
            pass_button = si.spell_maker("Pass_Button")
            si.spell_click(pass_button, 0, 0.7, False)
        wait_next_round()

        free_friend("sparck")
        free_friend("pork")


#   Fight Beans
    def part_two():
        global round_number
        global enchanted
        si.print_cool_way("Round Number " + str(round_number))
        try_to_enchant(1)
        try_to_enchant(2)

        def check_round():
            spells = ["Extract_Pig__Enchanted_Witch's_House_Call", 
                      "Extract_Pig_Enchanted_Celestial_Calendar" ,
                      "Extract_Pig_Enchanted_Ninja_Pigs"]

            if (round_number == 3):
                for i in spells:
                    if si.check_for_card(i) == True:
                        cast_spell(i, None)
                        cast_on_beans(i)
                        return False
                    
        if check_round() == False:
            return
        
        discard_list = ["Reshuffle", "Frenzy", "Myth_Prism", "Clear_Mind"]
        if enchanted == True:
            feint = "Feint"
            discard_list.append("Potent_Trap")
        else:
            feint = "Potent_Trap_Enchanted_Feint"
        while si.check_for_card(feint) == False:
            try_to_discard(discard_list)
            try_to_enchant(1)
            round_number += 1
            if check_round() == False:
                return

        if si.check_for_card("Beans_Shield") == True:
            pass_button = si.spell_maker("Pass_Button")
            si.spell_click(pass_button, 0, 0.7, False)
            wait_next_round()
            check_round()

        if enchanted == True:
            feint = "Feint"
        elif enchanted == False:
            feint = "Potent_Trap_Enchanted_Feint"
        cast_spell(feint, None)
        cast_on_beans("Feint")
        wait_next_round()
        spells = ["Extract_Pig_Enchanted_Witch's_House_Call", 
                  "Extract_Pig_Enchanted_Celestial_Calendar",
                  "Extract_Pig_Enchanted_Ninja_Pigs"]

        for i in spells:
            if si.image_search(si.spell_maker(i), 0.9) != None:
                cast_spell(i, None)
                cast_on_beans(i)
        wait_next_round()

    def part_three():
        def attempt_to_reshuffle():
            global battle_reshuffle
            si.pass_round()
            si.wait_for_image("Pass_Button")
            if si.check_for_card("Reshuffle") == True:
                si.spell_click(si.spell_maker("Reshuffle"), 0, 0.7, True)
                si.cast_on_yourself()
            si.wait_for_image("Pass_Button")
            if battle_reshuffle > 1:
                try_to_discard(["reshuffle"])
                battle_reshuffle -= 1

        def switch_to_balance():
            position = si.image_search(si.spell_maker("Yourself"), 0.8)
            if position != None:
                x,y = position
                x += 130
                y -= 45
                pya.moveTo(x, y, 0.5, pya.easeOutQuad)
                time.sleep(0.5)
                pya.click()
                time.sleep(0.5)
                pya.moveTo(x, y - 25, 0.5, pya.easeOutQuad)
                time.sleep(0.5)
                pya.click()
        
        position = si.image_search(si.spell_maker("Eye"), 0.9)
        if position != None:
            x,y = position
            pya.moveTo(x + 135, y - 24, 0.5, pya.easeOutQuad)
            time.sleep(1)
            pya.click()
            time.sleep(1)
            si.spell_click(si.spell_maker("Yes_Button"), 0, 0.7, False)

        switch_to_balance()

        def check_medulla_stats():
            medulla = si.spell_maker("Myth_Symbol")
            if si.image_search(medulla, 0.6) != None:
                position = si.image_search(medulla, 0.6)
                x, y = position
                pya.moveTo(x + 25, y)

        def check_if_dead():
            Pass_Button = si.spell_maker("Pass_Button")
            dead = False
            Spell_Book = si.spell_maker("Spell_Book")
            position = si.image_search(Pass_Button, 0.7)
            while position == None:
                #If the pass button shows, then they're alive, if the spellbook shows, they're dead
                position = si.image_search(Pass_Button, 0.7)
                if (position != None):
                    dead = False
                    break
                time.sleep(1)
                position = si.image_search(Spell_Book, 0.7)
                if (position != None):
                    dead = True
                    exit
                time.sleep(1)
            return dead
        
        def vaporize():
            global vaporizes
            if si.check_for_card("Unready_Draw_Button") == True:
                try_to_discard(["Medusa", "Ninja_Pigs", "Frenzy", "Extract_Pig_Enchanted_Medusa",
                                "Extract_Pig_Enchanted_Ninja_Pigs","Extract_Pig"])
            si.spell_click(si.spell_maker("Draw_Button"), 0, 0.7, False)
            cast_spell("Vaporize_Treasure_Card", "medulla")
            vaporizes -= 1
            print("Vaporizes Left: " + str(vaporizes))

        def check_card(spell):
            spell = si.spell_maker(spell)
            position = si.image_search(spell, 0.8)
            if position != None:
                return True
            else:
                return False
            
        while check_if_dead() == False:
            check_medulla_stats()
            dispel = si.spell_maker("Vaporize")
            feint = si.spell_maker("Feint")
            check_dispel = si.image_search(dispel, 0.9)
            check_feint = si.image_search(feint, 0.9)
            deck_feint = si.check_for_card("Feint")
            deck_potent_feint = si.check_for_card("Potent_Trap_Enchanted_Feint")
            deck_reshuffle = si.check_for_card("Reshuffle")

            if ((check_dispel) != None) and (check_feint != None):
                vaporize()
            elif ((check_dispel) != None) and (deck_potent_feint == True) and (deck_feint == True):
                cast_spell("Feint", "medulla")   
            elif ((check_dispel) != None) and (check_feint == None) and (deck_feint == True):
                cast_spell("Feint", "medulla") 
            elif (check_dispel != None) and (check_feint == None) and (deck_reshuffle == True):
                attempt_to_reshuffle()
            else:
                vaporize()

    part_one()
    part_two()
    part_three()

final_fight()
#   Fight Medulla
#   Exit Dungeon