# Script to farm Paralysis Tower EXP

import pyautogui
import time
import keyboard

# Define the coordinates to click (x, y)
coordinates = [
    (1114, 1057),  # 0 - Click Create
    (1822,  784),  # 1 - Click Room Scrollbar (then drag down)
    (1089,  891),  # 2 - Click Paralysis Tower
    (1149, 1173),  # 3 - Click Confirm
    (2244, 1051),  # 4 - Click Start
    (1410,  761),  # 5 - Click Cancel Reshuffle
    (2191,  961),  # 6 - Click Auto Play
    (2487,   91),  # 7 - X out of Stage 2
]

# How far to drag the scrollbar down (in pixels)
SCROLL_DRAG_Y = 100

# How long to wait for the battle to finish (seconds)
BATTLE_WAIT_SECONDS = 150  # 2 minutes 30 seconds


def wait_with_exit_check(seconds):
    """
    Wait for 'seconds' seconds, but check every 0.5s if 'E' is pressed to exit.
    """
    end_time = time.time() + seconds
    while time.time() < end_time:
        if keyboard.is_pressed('e'):
            print("E pressed during wait - exiting loop.")
            raise KeyboardInterrupt
        time.sleep(0.5)


def main():
    # Safety feature: Move mouse to top-left corner to abort
    pyautogui.FAILSAFE = True

    # Give user time to switch to the target window
    print("You have 5 seconds to switch to your target window...")
    print("Press 'E' key at any time to stop the script.")
    time.sleep(5)

    try:
        print("Starting the clicking sequence. Press 'E' to exit.")

        while not keyboard.is_pressed('e'):

            # 1) Click Create
            print(f"Clicking Create: {coordinates[0]}")
            pyautogui.click(*coordinates[0])
            time.sleep(1)

            # 2) Click Room Scrollbar and drag down 100px
            scrollbar_x, scrollbar_y = coordinates[1]
            print(f"Clicking and dragging scrollbar from: {coordinates[1]} down {SCROLL_DRAG_Y}px")
            pyautogui.moveTo(scrollbar_x, scrollbar_y)
            pyautogui.mouseDown()
            pyautogui.moveTo(scrollbar_x, scrollbar_y + SCROLL_DRAG_Y, duration=0.3)
            pyautogui.mouseUp()
            time.sleep(1)

            # 3) Click Paralysis Tower
            print(f"Clicking Paralysis Tower: {coordinates[2]}")
            pyautogui.click(*coordinates[2])
            time.sleep(1)

            # 4) Click Confirm
            print(f"Clicking Confirm: {coordinates[3]}")
            pyautogui.click(*coordinates[3])
            time.sleep(1)

            # 5) Click Start
            print(f"Clicking Start: {coordinates[4]}")
            pyautogui.click(*coordinates[4])
            time.sleep(1)

            # 6) Click Cancel Reshuffle
            print(f"Clicking Cancel Reshuffle: {coordinates[5]}")
            pyautogui.click(*coordinates[5])
            time.sleep(1)

            # 7) Click Auto Play
            print(f"Clicking Auto Play: {coordinates[6]}")
            pyautogui.click(*coordinates[6])
            time.sleep(1)

            # 8) Wait for battle to finish (2m 30s), with E-check
            print(f"Waiting {BATTLE_WAIT_SECONDS} seconds for the battle to finish...")
            wait_with_exit_check(BATTLE_WAIT_SECONDS)

            # 9) Click X out of Stage 2 once
            print(f"Clicking X out of Stage 2 (first time): {coordinates[7]}")
            pyautogui.click(*coordinates[6])
            time.sleep(3)

            # 10) Click X out of Stage 2 again
            print(f"Clicking X out of Stage 2 (second time): {coordinates[7]}")
            pyautogui.click(*coordinates[7])
            time.sleep(1)

            print("Sequence completed, starting again...\n")

    except KeyboardInterrupt:
        print("\nScript terminated by user.")
    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    main()
