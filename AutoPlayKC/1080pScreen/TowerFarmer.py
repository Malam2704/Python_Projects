# Script to farm the Normal Ascension Tower Stage (1080p resolution)
import pyautogui
import time
import keyboard

# Define your two coordinates (x, y)
coordinates = [
    (1487, 767),  # First point
    (1644, 747)   # Second point
]

def main():
    pyautogui.FAILSAFE = True  # Move mouse to top-left corner to stop script

    print("You have 5 seconds to switch to your target window...")
    print("Press 'E' at any time to stop the script.")
    time.sleep(5)

    try:
        while not keyboard.is_pressed('e'):
            # Click first coordinate
            print(f"Clicking first point: {coordinates[0]}")
            pyautogui.click(coordinates[0][0], coordinates[0][1])

            time.sleep(2.25)  # Wait 2.25 seconds

            # Click second coordinate
            print(f"Clicking second point: {coordinates[1]}")
            pyautogui.click(coordinates[1][0], coordinates[1][1])

            print("Waiting 2 minutes before repeating...")
            time.sleep(70)  # Wait 1.16 minutes

            pyautogui.click(coordinates[0][0], coordinates[0][1])
            time.sleep(2)  # Wait 2.25 seconds

            pyautogui.moveTo(coordinates[1][1], coordinates[0][1])


    except KeyboardInterrupt:
        print("\nScript manually terminated.")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
