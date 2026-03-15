# KingsCallDailyBot

This folder contains a screenshot-driven desktop automation starter for Steam and King's Call.

The approach is:

1. Launch Steam or the game.
2. Wait for specific UI images to appear.
3. Click the center of those images in order.
4. Optionally run at a daily time.

This is more reliable than hard-coded coordinates because you can update a few template images when the UI changes.

## Files

- `bot.py`: main automation runner
- `config.example.json`: example configuration
- `requirements.txt`: Python packages used by the bot
- `templates/`: put your screenshot snippets here

## Setup

1. Install dependencies:

```bash
cd /Users/mohammedalam/Documents/Projects/Python_Projects/KingsCallDailyBot
python3 -m pip install -r requirements.txt
```

2. Copy the example config:

```bash
cp /Users/mohammedalam/Documents/Projects/Python_Projects/KingsCallDailyBot/config.example.json /Users/mohammedalam/Documents/Projects/Python_Projects/KingsCallDailyBot/config.json
```

3. Add your screenshot snippets to:

`/Users/mohammedalam/Documents/Projects/Python_Projects/KingsCallDailyBot/templates`

Use tight crops around the exact clickable button text/icon, for example:

- `steam_play.png`
- `launcher_play.png`
- `daily_loot.png`
- `guild.png`
- `donate.png`
- `confirm.png`

4. Edit `config.json` to match your timing, launch method, and step order.

## Running

Run immediately:

```bash
python3 /Users/mohammedalam/Documents/Projects/Python_Projects/KingsCallDailyBot/bot.py --config /Users/mohammedalam/Documents/Projects/Python_Projects/KingsCallDailyBot/config.json --run-now
```

Wait until the configured daily time:

```bash
python3 /Users/mohammedalam/Documents/Projects/Python_Projects/KingsCallDailyBot/bot.py --config /Users/mohammedalam/Documents/Projects/Python_Projects/KingsCallDailyBot/config.json
```

Dry run without clicking:

```bash
python3 /Users/mohammedalam/Documents/Projects/Python_Projects/KingsCallDailyBot/bot.py --config /Users/mohammedalam/Documents/Projects/Python_Projects/KingsCallDailyBot/config.json --run-now --dry-run
```

## Config notes

### Launch modes

- `command`: run any command list you provide
- `steam_uri`: open a Steam URI such as `steam://rungameid/<APP_ID>`
- `none`: do not launch anything, just begin image matching

### Step behavior

Each step can:

- wait for an image to appear
- click it one or more times
- skip if marked optional
- add small delays between actions

You can also add `sleep` steps if the game needs a fixed pause between screens.

## Screenshot tips

- Capture templates at the same resolution and display scaling you will use when the bot runs.
- Crop tightly around the unique part of the button.
- Avoid large backgrounds around the button.
- If matching fails, lower confidence slightly, for example from `0.92` to `0.86`.
- Keep the game window in the same position each day if possible.

## macOS scheduling

For reliable once-a-day runs, use `launchd` instead of leaving a terminal open all day. The bot supports both styles:

- simplest: schedule `bot.py --run-now` with `launchd`
- fallback: start `bot.py` manually and let it wait for `daily_time`

If you want, I can add a ready-to-load `launchd` plist after you provide the exact run time and whether you want Steam opened by URI or by app name.
