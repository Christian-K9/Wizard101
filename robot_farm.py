import spell_index as si
import pyautogui as pya
import time

si.print_cool_way("Now Starting Robot Farm")
time.sleep(3)
#si.print_cool_way("Minimizing Window")
#pya.hotkey("win", "down")
#time.sleep(5)
si.game_click()
time.sleep(2)
si.aot_victory()
attempt = 0
while True:
    starting_point  = time.time()
    attempt += 1
    si.print_cool_way1("Attempt: " + str(attempt), 0.1)
    si.two_round_battle("Sharpened_Blade", "Myth_Blade", "Extract_Robot", "Orthrus", "aot_battle")
    ending_point = time.time()
    si.print_cool_way("Time: " + str(ending_point - starting_point))