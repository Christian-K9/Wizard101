import keyboard
import time
import sys
import pyautogui  # Ensure pyautogui is imported

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

# Simulates pressing a key for a specific duration
def press_key_for_duration(key, duration):
    start_time = time.perf_counter()
    pyautogui.keyDown(key)
    
    while (time.perf_counter() - start_time) < duration:
        pass
    
    pyautogui.keyUp(key)
    end_time = time.perf_counter()

    # Check the actual duration
    print(f"Actual time held: {end_time - start_time:.6f} seconds")

# Function to track key presses
def check_keys():
    global last_movement
    while True:
        for key in keys_state:
            if keyboard.is_pressed(key):
                if not keys_state[key]['pressed']:  # Key was not pressed before, now it is
                    keys_state[key]['pressed'] = True
                    keys_state[key]['pressed_at'] = time.time()
                    log_event(key, "Pressed")
                    last_movement = time.time()
            else:
                if keys_state[key]['pressed']:  # Key was pressed before, now it's released
                    keys_state[key]['pressed'] = False
                    released_at = time.time()
                    duration = released_at - keys_state[key]['pressed_at']
                    log_event(key, "Released", duration)
                    last_movement = time.time()
        # Small delay to prevent CPU overload
        time.sleep(0.01)

# Prints the log of all events and exits
def print_log():
    print("\nEvery Key Pressed: ")
    for event in logging_events:
        print(event)
    sys.exit()

# Main loop setup
print("Press 'W', 'A', 'S', 'D' for movement logging. Press 'q' to exit.")
keyboard.add_hotkey('q', print_log)  # Exit when 'q' is pressed

# Run the key tracking
check_keys()
