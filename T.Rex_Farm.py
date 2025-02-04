import spell_index as si
import time
import pyautogui as pya

si.print_cool_way("Now Starting Dr. T. Rex Farm")
time.sleep(3)

while True:
    si.game_click()
    si.wait_for_image("Clearing_Symbol")
    pya.keyDown("X")
    time.sleep(0.5)
    pya.keyUp("X")
    time.sleep(20)
    pya.keyDown("W")
    time.sleep(7)
    pya.keyUp("W")
    si.wait_for_image("Pass_Button")
    si.two_round_battle("Sharpened_Blade", "Myth_Blade", "Extract_Dino", "Orthrus", None)
    si.game_click()
    pya.keyDown("A")
    time.sleep(0.47)
    pya.keyUp("A")
    time.sleep(1)
    pya.keyDown("W")
    time.sleep(5)
    pya.keyUp("W")
    time.sleep(10)
    pya.keyDown("S")
    time.sleep(0.5)
    pya.keyUp("S")

    