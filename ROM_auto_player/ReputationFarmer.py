# Script to farm reputation points in the game for Elves

import pyautogui
import time

# Define the coordinates to click (x, y)
coordinates = [
    (1167, 479),  # First point
    (1576, 843),  # Second point
    (1901, 905),  # Third point
    (1279, 684)   # Fourth point
]

# Delay between clicks in seconds
delay = 3

# Number of times to repeat the sequence
repeat_times = 5

def main():
    # Safety feature: Move mouse to top-left corner to abort
    pyautogui.FAILSAFE = True
    
    # Give user time to switch to the target window
    print("You have 5 seconds to switch to your target window...")
    time.sleep(5)
    
    try:
        print(f"Starting to click at {len(coordinates)} points, repeating {repeat_times} times...")
        
        for i in range(repeat_times):
            print(f"Sequence {i+1}/{repeat_times}")
            
            # Click each coordinate in sequence
            for j, (x, y) in enumerate(coordinates):
                print(f"Clicking point {j+1}: ({x}, {y})")
                pyautogui.click(x, y)
                time.sleep(delay)
                
        print("Click sequence completed!")
            
    except KeyboardInterrupt:
        print("\nScript terminated by user.")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()