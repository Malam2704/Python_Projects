# Script to farm Battlements (1080p resolution)
import pyautogui
import time
import keyboard

# Define the coordinates to click (x, y) for Battlements flow (1080p)
# Update these three coordinates based on your screenshots.
coordinates = [
    (0, 0),  # 0 - Click Battlements entry
    (0, 0),  # 1 - Click target option
    (0, 0),  # 2 - Click confirm/start for Battlements
    (1058, 571),  # 3 - Click Cancel Reshuffle (from ParalysisEXP.py)
    (1643, 721),  # 4 - Click Auto Play (from ParalysisEXP.py)
]

# How many runs to execute
RUN_COUNT = 3

# How long to wait after starting auto play (seconds)
BATTLE_WAIT_SECONDS = 150


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
        print("Starting Battlements sequence. Press 'E' to exit.")

        for run_index in range(RUN_COUNT):
            if keyboard.is_pressed('e'):
                break

            print(f"Run {run_index + 1} of {RUN_COUNT}")

            # 1) Click Battlements entry
            print(f"Clicking Battlements entry: {coordinates[0]}")
            pyautogui.click(*coordinates[0])
            time.sleep(1)

            # 2) Click target option
            print(f"Clicking target option: {coordinates[1]}")
            pyautogui.click(*coordinates[1])
            time.sleep(1)

            # 3) Click confirm/start
            print(f"Clicking confirm/start: {coordinates[2]}")
            pyautogui.click(*coordinates[2])
            time.sleep(1)

            # 4) Click Cancel Reshuffle
            print(f"Clicking Cancel Reshuffle: {coordinates[3]}")
            pyautogui.click(*coordinates[3])
            time.sleep(1)

            # 5) Click Auto Play
            print(f"Clicking Auto Play: {coordinates[4]}")
            pyautogui.click(*coordinates[4])
            time.sleep(1)

            # 6) Wait for battle to finish
            print(f"Waiting {BATTLE_WAIT_SECONDS} seconds for the battle to finish...")
            wait_with_exit_check(BATTLE_WAIT_SECONDS)

            print("Run completed.\n")

    except KeyboardInterrupt:
        print("\nScript terminated by user.")
    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    main()
