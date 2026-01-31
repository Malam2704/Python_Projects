# AutoPlayKC (1080p)

## Step-by-step Linux setup (run inside 1080pScreen)

1) Go to the folder:
```
cd /home/mohammed/Desktop/Python_Projects/AutoPlayKC/1080pScreen
```

2) Create the virtual environment (one time):
```
python3 -m venv .venv
```

3) Activate the virtual environment (every new terminal):
```
source .venv/bin/activate
```

4) Upgrade pip:
```
python -m pip install --upgrade pip
```

5) Install Python dependencies:
```
pip install pyautogui keyboard
```

6) Run a script:
```
python Battlements.py
# or
python ParalysisEXP.py
```

## Optional system dependencies (Ubuntu/Debian)
If PyAutoGUI errors, install these:
```
sudo apt-get update
sudo apt-get install -y python3-tk python3-dev scrot
```

## Linux note about the keyboard library
On Linux, the `keyboard` package requires root. If you see an error like
"must be root", you have two options:

- Run the script with sudo:
```
sudo -E /home/mohammed/Desktop/Python_Projects/AutoPlayKC/1080pScreen/.venv/bin/python Battlements.py
```

- Or replace `keyboard` with a non-root hotkey library (like `pynput`).
