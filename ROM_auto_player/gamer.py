import datetime
import time
import subprocess
import pyautogui

# ================================
# Configuration (customize these)
# ================================

# Set the target time (24-hour format) when the game should launch.
TARGET_HOUR = 14    # Example: 14 for 2 PM
TARGET_MINUTE = 0   # Example: 0 minutes
TARGET_SECOND = 0   # Example: 0 seconds

# Path to your game executable (update this with the actual path)
GAME_EXECUTABLE = r"C:\Path\To\Your\Game.exe"

# List of (x, y) coordinates where the clicks will occur
# Adjust these coordinates to the locations in your game where actions occur.
CLICK_COORDINATES = [
    (100, 200),  # Example coordinate for the first task (e.g., click "collect soul stones")
    (150, 250),  # Example coordinate for the second task
    # Add additional coordinates as needed
]

# Time delays (in seconds) to allow for game load and between actions
GAME_LOAD_DELAY = 10  # Time to wait for the game to fully load
CLICK_DELAY = 2       # Delay between each click
POST_CLICK_DELAY = 5  # Extra delay after clicking before exiting the game

# ================================
# Wait until the target time
# ================================
print("Waiting for the target time...")

while True:
    now = datetime.datetime.now()
    if (now.hour == TARGET_HOUR and 
        now.minute == TARGET_MINUTE and 
        now.second >= TARGET_SECOND):
        break
    time.sleep(1)

print("Target time reached. Launching the game...")

# ================================
# Launch the game
# ================================
# This launches the game process; update GAME_EXECUTABLE with your game's path.
game_process = subprocess.Popen([GAME_EXECUTABLE])

# Wait for the game to load completely
time.sleep(GAME_LOAD_DELAY)

# ================================
# Perform in-game tasks
# ================================
print("Game launched. Performing tasks...")

# Loop over each set of coordinates and simulate a mouse click
for idx, (x, y) in enumerate(CLICK_COORDINATES):
    print(f"Clicking at coordinate {idx + 1}: ({x}, {y})")
    pyautogui.click(x, y)
    time.sleep(CLICK_DELAY)

# Optional: Wait for soul stones to be collected or any other in-game event
time.sleep(POST_CLICK_DELAY)

# ================================
# Exit the game
# ================================
print("Tasks complete. Exiting the game...")

# Option 1: Simulate a hotkey (Alt+F4) to close the game
pyautogui.hotkey('alt', 'f4')

# Option 2: Alternatively, terminate the game process directly
game_process.terminate()

print("Game exited. Script complete.")
