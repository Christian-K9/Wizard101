import spell_index as si
import pyautogui as pya
import keyboard
import time

time.sleep(3)
#si.game_click()
#keyboard.press("x")
#si.spell_click(si.spell_maker("Dance_Game_Wizard_City_Symbol"), 0, 0.7, False)
#time.sleep(1)
#si.spell_click(si.spell_maker("Play_Button_Symbol"), 0, 0.7, False)
#time.sleep(1)

def arrow_detector():
    movements = []
    arrows = ["Up", "Down", "Left", "Right"]
    position = si.check_for_card("Go_Symbol")
    while position == False:
        for i in arrows:
            symbol = "Dance_Game_" + i + "_Arrow"
            if si.image_search(si.spell_maker(symbol), 0.7) != None:
                movements.append(i.lower())
                si.wait_for_image("Blank_Symbol")
                position = si.check_for_card("Go_Symbol")

    return movements

def dance_response(movements):
    for i in movements:
        print("Movement: " + i)
        keyboard.press(i)
        time.sleep(1)

while (si.check_for_card("Done_Symbol") == False):
    si.wait_for_image("Match_This_Symbol")
    print("Starting Game")
    dance_response(arrow_detector())
    if si.check_for_card("Next_Button") == True:
        break
