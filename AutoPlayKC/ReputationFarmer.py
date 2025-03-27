# Script to farm reputation points in the game for Elves

import pyautogui
import time
import keyboard

# Define the coordinates to click (x, y)
coordinates = [
    (1176, 522),
    # (1167, 479),  # First point
    (1576, 843),  # Second point
    (1901, 905),  # Third point
    (1279, 684)   # Fourth point
]

# Time to wait before clicking the fourth point (in seconds)
# 1 minute and 30 seconds = 90 seconds
wait_time = 50

def main():
    # Safety feature: Move mouse to top-left corner to abort
    pyautogui.FAILSAFE = True
    
    # Give user time to switch to the target window
    print("You have 5 seconds to switch to your target window...")
    print("Press 'E' key at any time to stop the script")
    time.sleep(5)
    
    try:
        print("Starting the clicking sequence. Press 'E' to exit.")
        
        # Keep running until 'E' is pressed
        while not keyboard.is_pressed('e'):
            # Click the first 3 coordinates
            for i in range(3):
                print(f"Clicking point {i+1}: {coordinates[i]}")
                pyautogui.click(coordinates[i][0], coordinates[i][1])
                time.sleep(0.5)  # Small delay between consecutive clicks
            
            # Wait for the specified time
            print(f"Waiting for {wait_time} seconds before clicking the fourth point...")
            
            # Check for 'E' key during the wait period
            start_time = time.time()
            while time.time() - start_time < wait_time:
                if keyboard.is_pressed('e'):
                    print("E key pressed, exiting...")
                    return
                time.sleep(0.1)
            
            # Click the fourth point
            print(f"Clicking point 4: {coordinates[3]}")
            pyautogui.click(coordinates[3][0], coordinates[3][1])
            time.sleep(0.5)
            
            print("Sequence completed, starting again...")
            
    except KeyboardInterrupt:
        print("\nScript terminated.")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()