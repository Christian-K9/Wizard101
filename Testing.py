import os
import sys
import time

import os
import sys
import threading
import time
import keyboard  # Install with: pip install keyboard

def stop_program():
    """Exit the program completely."""
    print("\nStopping program...")
    os._exit(0)  # Hard exit


def restart_program():
    """Restart the current Python script."""
    print("Restarting program...")
    python = sys.executable
    os.execv(python, [python] + sys.argv)  # Fully restarts the script

def main_program():
    """Main loop to simulate program running."""
    i = 1
    while True:
        print(f"Program running... ({i})")
        time.sleep(1)
        i += 1

def listen_for_exit():
    """Listen for 'q' to restart, or 'e' to exit completely."""
    print("Press 'Q' to restart, 'E' to exit...")
    while True:
        if keyboard.is_pressed("q"):
            print("\n'Q' pressed. Restarting...")
            restart_program()
        elif keyboard.is_pressed("e"):
            print("\n'E' pressed. Exiting...")
            stop_program()


if __name__ == "__main__":
    # Start the key listener in a separate thread
    listener_thread = threading.Thread(target=listen_for_exit, daemon=True)
    listener_thread.start()

    # Start the main program
    main_program()
