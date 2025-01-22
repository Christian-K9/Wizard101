import pyautogui as pya
import time
import spell_index as si

reshuffle = 4
def try_to_discard(possible_discards):
    global reshuffle
    card_check = False
    for i in possible_discards:
        if si.check_for_card(i) == True:
            if ((i == "Reshuffle") or (i == "Unready_Reshuffle")):
                if reshuffle <= 1:
                    print("Discarded Too Many Reshuffles")
                    continue
                else:
                    reshuffle -=1
            print("Reshuffles Left: " + str(reshuffle))
            si.discard_card(i)
            card_check = True
        else:
            print(str(i) + " Not Found")
    return card_check

def switch_to_balance():
    position = si.image_search(si.spell_maker("Yourself"), 0.7)
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

def outfit_equip(outfit_number):
    pya.keyDown("ctrl")
    time.sleep(0.3)
    pya.keyDown(outfit_number)
    time.sleep(0.3)
    pya.keyUp("ctrl")
    time.sleep(0.3)
    pya.keyUp(outfit_number)

def cast_on_quizzler():
    quizzler = si.spell_maker("Myth_Symbol")
    if si.image_search(quizzler, 0.9) != None:
        position = si.image_search(quizzler, 0.9)
        x, y = position
        pya.moveTo(x + 25, y - 5, 0.5, pya.easeOutQuad)
        pya.click()

def find_beans_1(click):
    beans = si.spell_maker("Beans_Name")
    position = si.image_search(beans, 0.9)
    if position != None:
        if click == True:
            si.spell_click(beans, 0, 0.7, 0)
        return True
    else:
        print("Find Beans 1: False")
        return False
    
def find_beans_2(click):
    beans = si.spell_maker("Life_Symbol")
    position = si.image_search(beans, 0.9)
    if position != None:
        print("Position: " + str(position))
        if click == True:
            x,y = position
            pya.moveTo(x + 30, y + 5, 0.5, pya.easeOutQuad)
            time.sleep(1)
            pya.click()
    else:
        print("Find Beans 2: False")
        return False


def find_beans_3():
    medulla = si.spell_maker("Myth_Symbol")
    enemies = ["dagger", "key", "gem", "spiral"]
    alive_enemies = []
    for i in enemies:
        enemy = si.spell_maker(i)
        if si.image_search(enemy, 0.7) != None:
            alive_enemies.append(enemy)
    print("Alive Enemies: " + str(alive_enemies))
    print("Alive Enemies: " + str(len(alive_enemies)))
    beans_find = find_beans_4(alive_enemies[0])
    if len(alive_enemies) != 2 and beans_find == False:
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


def check_beans_feint():
    time.sleep(1)
    beans = si.spell_maker("Life_Symbol")
    position = si.image_search(beans, 0.6)
    if position != None:
        x,y = position
        pya.moveTo(x + 5, y + 30, 0.5, pya.easeOutQuad)
        feint = si.spell_maker("Beans_Feint")
        position = si.image_search(feint, 0.9)
        if position != None:
            return True
    return False


def cast_on_medulla():
    medulla = si.spell_maker("Myth_Symbol")
    if si.image_search(medulla, 0.6) != None:
        position = si.image_search(medulla, 0.6)
        x, y = position
        pya.moveTo(x + 25, y - 5, 0.5, pya.easeOutQuad)
        pya.click()

def quizzler_battle():
    si.wait_for_image("Pass_Button")
    myth_prism = si.spell_maker("Myth_Prism")
    si.spell_click(myth_prism, 0, 0.7, True)
    cast_on_quizzler()
    si.wait_for_image("Pass_Button")
    si.enchant_card("Epic", "Orthrus")
    orthrus = si.spell_maker("Epic_Enchanted_Orthrus")
    si.spell_click(orthrus, 0, 0.7, True)
    si.wait_for_image("More_Button")

def try_to_enchant(spell, enchant):
    if (si.check_for_card(spell) == True) and (si.check_for_card(enchant) == True):
        si.enchant_card(enchant, spell)
        return True
    else:
        return False

def enter_dungeon():
    si.game_click()
    time.sleep(3)
    si.wait_for_image("Headquarters_Symbol")
    pya.press("x")
    time.sleep(20)
    si.wait_for_image("Spell_Book")
    time.sleep(3)
    pya.keyDown('W')
    time.sleep(3.55)
    pya.keyUp('W')
    pya.keyDown('A')
    time.sleep(0.24)
    pya.keyUp('A')
    pya.keyDown('W')
    time.sleep(3.54)
    pya.keyUp('W')
    pya.keyDown('D')
    time.sleep(0.32)
    pya.keyUp('D')
    pya.keyDown('W')
    time.sleep(3.10)
    pya.keyUp('W')
    pya.keyDown('D')
    time.sleep(0.33)
    pya.keyUp('D')
    pya.keyDown('W')
    time.sleep(4.12)
    pya.keyUp('W')
    time.sleep(1)
    pya.keyDown('W')
    time.sleep(3)
    pya.keyUp('W')

    time.sleep(3)

def part_two():
     pya.keyDown('D')
     time.sleep(0.2)
     pya.keyUp('D')
     time.sleep(1)
     pya.keyDown('W')
     time.sleep(6.3)
     pya.keyUp('W')
     time.sleep(1)
     pya.keyDown('A')
     time.sleep(0.2)
     pya.keyUp('A')
     time.sleep(1)
     pya.keyDown('W')
     time.sleep(5.0)
     pya.keyUp('W')
     time.sleep(1)
     pya.keyDown('D')
     time.sleep(0.2)
     pya.keyUp('D')
     time.sleep(1)
     pya.keyDown('W')
     time.sleep(5)
     pya.keyUp('W')

     si.wait_for_image("Pass_Button")
     part_two_fight()

def part_one():

    si.print_cool_way("Equipping First Battle Deck")
    outfit_equip("2")
    si.print_cool_way("Make Sure You Are Standing In Front Of The Signal")
    enter_dungeon()
    si.print_cool_way("Getting Ready For First Battle")

    si.wait_for_image("More_Button")

    More_Button = si.spell_maker("More_Button")
    Done_Button = si.spell_maker("Done_Button")

    for i in range(0,4):
        si.spell_click(More_Button, 0, 0.9, False)
        time.sleep(2)

    si.spell_click(Done_Button, 0, 0.7, False)
    time.sleep(3)
    pya.keyDown("w")
    time.sleep(3)
    pya.keyUp("w")

    quizzler_battle()

    si.spell_click(More_Button, 0, 0.9, False)
    time.sleep(2)
    si.spell_click(Done_Button, 0, 0.7, False)
    time.sleep(3)

def part_two_fight():


    #Strategy:
    #   1. Cast Frenzy
    #   2. Free Pork
    #   3. Free Sparck
    #   4. Hit Beans With Ninja Pigs
    #   5. Place Enchanted Feint on Beans
    #   6. Vaporize Medulla Until Cannon Defeats Him

    def cast_on_beans():
        find_beans_1(True)
        find_beans_2(True)
        find_beans_3()

    def check_on_beans():
        if (((find_beans_1(False) == False) and (find_beans_2(False) == False) and (find_beans_3() == False)) == True):
            return False
        else:
            return True
    def attempt_to_reshuffle():
        while si.check_for_card("Unready_Reshuffle") == True:
            si.pass_round()
            si.wait_for_image("Pass_Button")
        si.spell_click(si.spell_maker("Reshuffle"), 0, 0.7, True)
        si.cast_on_yourself()

    def free_friends(friend):
        clear_mind = si.spell_maker("Clear_Mind")
        si.spell_click(clear_mind, 0, 0.7, False)
        if si.image_search(friend, 0.6) != None:
            position = si.image_search(friend, 0.6)
            x, y = position
            pya.moveTo(x + 25, y - 5, 0.5, pya.easeOutQuad)
            pya.click()
    
    def beans_fight():

        si.print_cool_way("Attempting To Fight Beans")
        spells = {"Witch's_House_Call": "Extract_Pig", "Celestial_Calendar": "Extract_Pig"}

        extras = []
        for i in spells:
            if try_to_enchant(i, spells[i]) == True:
                extras.append(True)

        if len(extras) <= 0:
            try_to_discard(["Clear_Mind", "Frenzy", "Reshuffle"])

        calendar = "Extract_Pig_Enchanted_Celestial_Calendar"
        witch = "Extract_Pig_Enchanted_Witch's_House_Call"

        while si.check_for_card("Feint") == False:
            si.print_cool_way("Feint Not Found")
            try_to_discard(["Clear_Mind", "Frenzy", "Reshuffle"])
            si.pass_round()
            si.wait_for_image("Pass_Button")
        
        si.wait_for_image("Pass_Button")
        time.sleep(1)
        while (check_on_beans() and check_beans_feint()):
            print("Attempting To Feint Beans")
            if si.check_for_card("Feint") == True:
                si.spell_click(si.spell_maker("Feint"), 0, 0.7, True)
                cast_on_beans()
                si.wait_for_image("Pass_Button")
            for i in spells:
                if try_to_enchant(i, spells[i]) == True:
                    extras.append(True)
            time.sleep(1)
        
        while (si.check_for_card(witch) == False) and (si.check_for_card(calendar) == False) and (check_on_beans() == True):
            try_to_discard(["Frenzy", "Reshuffle"])
            si.pass_round()
            si.wait_for_image("Pass_Button")
            for i in spells:
                if try_to_enchant(i, spells[i]) == True:
                    extras.append(True)

        
        beans = ("Life_Symbol")

        si.print_cool_way("Card Ready")

        beans_status = si.image_search(si.spell_maker(beans), 0.5)
        print("Witch Status " + str(si.check_for_card(witch)))
        print("Calendar Status " + str(si.check_for_card(calendar)))

        while beans_status != None:
            if (si.check_for_card(witch) == True):
                si.spell_click(si.spell_maker(witch), 0, 0.7, True)
                cast_on_beans()
            elif si.check_for_card(calendar):
                si.spell_click(si.spell_maker(calendar), 0, 0.7, True)
                cast_on_beans()
            si.wait_for_image("Pass_Button")
            beans_status = si.image_search(si.spell_maker(beans), 0.6)



    def medulla_fight():
        switch_to_balance()

        position = si.image_search(si.spell_maker("Eye"), 0.7)
        if position != None:
            x,y = position
            pya.moveTo(x + 135, y - 24, 0.5, pya.easeOutQuad)
            time.sleep(1)
            pya.click()
            time.sleep(1)
            si.spell_click(si.spell_maker("Yes_Button"), 0, 0.7, False)

        def check_medulla_stats():
            medulla = si.spell_maker("Myth_Symbol")
            if si.image_search(medulla, 0.6) != None:
                position = si.image_search(medulla, 0.6)
                x, y = position
                pya.moveTo(x + 25, y + 10, 0.5, pya.easeOutQuad)

        def vaporize():
            if si.check_for_card("Unready_Draw_Button") == True:
                try_to_discard(["Witch's_House_Call", "Celestial_Calendar", "Frenzy", "Extract_Pig_Enchanted_Celestial_Calendar",
                                "Extract_Pig_Enchanted_Witch's_House_Call", "Unready_Witch's_House_Call", "Unready_Celestial_Calendar"
                                , "Extract_Pig"])
            si.spell_click(si.spell_maker("Draw_Button"), 0, 0.7, False)
            si.spell_click(si.spell_maker("Vaporize_Treasure_Card"), 0, 0.7, True)
            cast_on_medulla()

        dispel = "Headquarters_Dispel"
        feint = "Headquarters_Feint"

        #1. Try To Discard Unecessary Cards
        #2. If there is both a feint and a dispel, then vaporize
        #3. If there is a dispel, but no feint, with a feint in deck, then feint
        #4. If there is a dispel, but no feint, with no feint in deck, with a reshuffle, then reshuffle
        #5. If Nothing else then vaporize

        while (si.check_for_card("Spell_Book") == False):
            try_to_discard(["Witch's_House_Call", "Celestial_Calendar", "Frenzy", "Extract_Pig_Enchanted_Celestial_Calendar","Extract_Pig_Enchanted_Witch's_House_Call", "Clear_Mind", 
                            "Unready_Witch's_House_Call", "Unready_Celestial_Calendar"])
            check_medulla_stats()
            check_dispel = si.check_for_card(dispel)
            check_feint = si.check_for_card(feint)
            deck_feint = si.check_for_card("Feint")
            deck_reshuffle = si.check_for_card("Reshuffle")

            if ((check_dispel) == True) and (check_feint == True):
                vaporize()
            elif ((check_dispel) == True) and (check_feint != True) and (deck_feint == True):
                si.spell_click(si.spell_maker("Feint"))
                cast_on_medulla()
            elif (check_dispel == True) and (check_feint != True) and (deck_reshuffle == True):
                attempt_to_reshuffle()
            else:
                vaporize()
            si.wait_for_image("Pass_Button")
        
            
    spells = {"Witch's_House_Call": "Extract_Pig", "Celestial_Calendar": "Extract_Pig",}

    extras = []

    for i in spells:
        if try_to_enchant(i, spells[i]) == True:
            extras.append(True)

    card_check = True

    if len(extras) <= 0:
        card_check = try_to_discard(["Unready_Reshuffle"])

    elif card_check == False:
        try_to_discard(["Frenzy"])

    if si.check_for_card("Frenzy") == True:
        si.spell_click(si.spell_maker("Frenzy"), 0, 0.7, True)
        si.wait_for_image("Pass_Button")

    elif si.check_for_card("Feint") == True:
        si.spell_click(si.spell_maker("Feint"), 0, 0.7, True)
        cast_on_beans()
        si.wait_for_image("Pass_Button")
    
    else:
        si.pass_round()

    pork = si.spell_maker("Fire_Symbol")
    sparck = si.spell_maker("Balance_Symbol")
    si.wait_for_image("Pass_Button")

    while (si.image_search(pork, 0.6) != None):
        si.print_cool_way("Attempting To Free Pork")
        free_friends(pork) 
        si.wait_for_image("Pass_Button")

    while (si.image_search(sparck, 0.6) != None):
        si.print_cool_way("Attempting To Free Sparck")
        free_friends(sparck) 
        si.wait_for_image("Pass_Button")


    beans_fight()
    medulla_fight()

si.print_cool_way("Now Starting Headquarters Dungeon")
time.sleep(2)
si.game_click()
part_one()

si.print_cool_way("Now Starting Part Two Of Dungeon")
outfit_equip("1")
part_two()

