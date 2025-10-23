import pyautogui
import time
import keyboard

# Define your two coordinates (x, y)
coordinates = [
    (1133, 419),  # First point
    (1725, 881)   # Second point
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

            time.sleep(4)  # Wait 4 seconds

            # Click second coordinate
            print(f"Clicking second point: {coordinates[1]}")
            pyautogui.click(coordinates[1][0], coordinates[1][1])

            print("Waiting 2 minutes before repeating...")
            time.sleep(120)  # Wait 2 minutes

    except KeyboardInterrupt:
        print("\nScript manually terminated.")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
