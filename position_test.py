import spell_index as si
import pyautogui as pya
import time
import keyboard as key

def final_measure():
    time.sleep(1)
    medulla = si.spell_maker("Myth_Symbol")
    position = si.image_search(medulla, 0.7)
    if position != None:

        x_pos,y_pos = position
        print("X_Pos" + str(x_pos))
        x_points = [182, 437, 678, 924]
        difference = 1023
        coordinate = 0
        for x in x_points:
            print("Difference: " + str(difference))
            print("Max: " + str(max(x_pos,x)))
            print("Min: " + str(min(x_pos,x)))
            temp = max(x_pos, x) - min(x_pos, x)
            print("Temp" + str(temp))
            if temp < difference:
                difference = temp
                coordinate = x
            print("New Difference: " + str(difference))
            print()
            print()

        print("Difference:" + str(difference))
        for x in x_points:
            print(x)
            if x != coordinate:
                pya.moveTo(x, 82, 0.5, pya.easeOutQuad)
                pya.click()
                time.sleep(1)
            else:
                print("Not Clicking " + str(x)) 

def position_check():
    while True:
        if key.is_pressed("g"):
            position = pya.position()
            print(position)
            time.sleep(1)
        

final_measure()