# Script to farm reputation points in the game for Elves

import pyautogui
import time
import keyboard

# Define the coordinates to click (x, y)
coordinates = [
    (1274, 291),   # First point
    (1725, 881),   # Second point
    (2192, 996)    # Third point
]

def main():
    # Safety feature: Move mouse to top-left corner to abort
    pyautogui.FAILSAFE = True
    
    # Give user time to switch to the target window
    print("You have 5 seconds to switch to your target window...")
    print("Press 'E' key at any time to stop the script")
    time.sleep(5)
    
    try:
        print("Starting the clicking sequence. Press 'E' to exit.")
        
        while not keyboard.is_pressed('e'):
            # Click first coordinate
            print(f"Clicking point 1: {coordinates[0]}")
            pyautogui.click(coordinates[0][0], coordinates[0][1])
            
            time.sleep(1)  # Wait 1 seconds
            
            # Click second coordinate
            print(f"Clicking point 2: {coordinates[1]}")
            pyautogui.click(coordinates[1][0], coordinates[1][1])

            time.sleep(50)  # Wait 7 seconds
            
            # Click third coordinate
            print(f"Clicking point 3: {coordinates[2]}")
            pyautogui.click(coordinates[2][0], coordinates[2][1])
            
            time.sleep(1.5)  # Wait 1.5 seconds

            print("Sequence completed, starting again...")
            
    except KeyboardInterrupt:
        print("\nScript terminated.")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
