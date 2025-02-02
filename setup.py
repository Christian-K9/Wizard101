import subprocess
import sys
import spell_index as si
import time

def install_package(package):
    subprocess.check_call([sys.executable, "-m", "pip", "install", package])

library = ["pyautogui", "opencv-python", "numpy", "keyboard", "imagesearch"]

for i in library:
    si.print_cool_way("Attempting To Install " + i)
    install_package(i)
    print()
    time.sleep(2)