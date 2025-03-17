import pyautogui as pya
import keyboard as key
import sys

print("Starting Clicker Farm")
while True:
    minimum = sys.float_info.min
    if key.is_pressed("x"):
        pya.click(interval= minimum)