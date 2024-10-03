import keyboard
import time
import sys

# Track current key states and their timestamps
keys_state = {
    'w': {'pressed': False, 'pressed_at': None},
    'a': {'pressed': False, 'pressed_at': None},
    's': {'pressed': False, 'pressed_at': None},
    'd': {'pressed': False, 'pressed_at': None}
}

last_movement = time.time()
logging_events = []
# Logs key press/release events with timestamp
def log_event(key, action, duration=None):
    timestamp = time.time()
    if action == "Pressed":
        print(f"{timestamp:.2f} - {action}: {key.upper()}")
    elif action == "Released":
        log = (f"{timestamp:.2f} - {action}: {key.upper()} (held for {duration:.2f} seconds)")
        logging_events.append(log)
        print(log)

def check_keys():
    global last_movement
    while True:
        for key in keys_state:
            if keyboard.is_pressed(key):
                if not keys_state[key]['pressed']:  # Key was not pressed before, now it is
                    keys_state[key]['pressed'] = True
                    keys_state[key]['pressed_at'] = time.time()
                    log_event(key, "Pressed")
                    pressed_time = time.time()
                    last_movement = pressed_time
            else:
                if keys_state[key]['pressed']:  # Key was pressed before, now it's released
                    keys_state[key]['pressed'] = False
                    released_at = time.time()
                    duration = released_at - keys_state[key]['pressed_at']
                    log_event(key, "Released", duration)
                    released_time = time.time()
                    last_movement = released_time
        # Small delay to prevent CPU overload
        time.sleep(0.01)

def print_log():
    print()
    print("Every Key Pressed: ")
    for i in logging_events:
        print(i)
    sys.exit()

# Run the key checking function
print("Press 'W', 'A', 'S', 'D' for movement logging. Press 'q' to exit.")
keyboard.add_hotkey('q', print_log)  # Exit on ESC key press
check_keys()
