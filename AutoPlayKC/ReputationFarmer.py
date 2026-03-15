# Script to farm reputation points in the game for Elves (Mac Compatible)

import pyautogui
import time
from pynput import keyboard
import threading

# Define the coordinates to click (x, y)
coordinates = [
    (1598, 904),
    (2166, 1328),
    (2592, 1414),
    (1279, 684)   # Fourth point
]

# Time to wait before clicking the fourth point (in seconds)
wait_time = 50

# Global variable to control script execution
stop_script = False

def on_press(key):
    """Handle key press events"""
    global stop_script
    try:
        if key.char and key.char.lower() == 'e':
            print("\nE key detected, stopping script...")
            stop_script = True
    except AttributeError:
        # Special keys (like ctrl, alt, etc.) don't have char attribute
        pass

def main():
    global stop_script
    
    # Safety feature: Move mouse to top-left corner to abort
    pyautogui.FAILSAFE = True
    
    # Start keyboard listener in a separate thread
    listener = keyboard.Listener(on_press=on_press)
    listener.start()
    
    # Give user time to switch to the target window
    print("You have 5 seconds to switch to your target window...")
    print("Press 'E' key at any time to stop the script")
    time.sleep(5)
    
    try:
        print("Starting the clicking sequence. Press 'E' to exit.")
        
        # Keep running until 'E' is pressed
        while not stop_script:
            # Click the first 3 coordinates
            for i in range(3):
                if stop_script:
                    break
                print(f"Clicking point {i+1}: {coordinates[i]}")
                pyautogui.click(coordinates[i][0], coordinates[i][1])
                time.sleep(0.5)  # Small delay between consecutive clicks
            
            if stop_script:
                break
                
            # Wait for the specified time
            print(f"Waiting for {wait_time} seconds before clicking the fourth point...")
            
            # Check for stop signal during the wait period
            start_time = time.time()
            while time.time() - start_time < wait_time:
                if stop_script:
                    print("E key pressed, exiting...")
                    break
                time.sleep(0.1)
            
            if stop_script:
                break
                
            # Click the fourth point
            print(f"Clicking point 4: {coordinates[3]}")
            pyautogui.click(coordinates[3][0], coordinates[3][1])
            time.sleep(0.5)
            
            print("Sequence completed, starting again...")
            
    except KeyboardInterrupt:
        print("\nScript terminated by Ctrl+C.")
    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        # Clean up the keyboard listener
        listener.stop()
        print("Script stopped.")

if __name__ == "__main__":
    main()