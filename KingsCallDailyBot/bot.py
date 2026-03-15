from __future__ import annotations

import argparse
import datetime as dt
import json
import subprocess
import sys
import time
from pathlib import Path
from typing import Any, Iterable

import pyautogui


ROOT = Path(__file__).resolve().parent
DEFAULT_CONFIG = ROOT / "config.json"

pyautogui.FAILSAFE = True
pyautogui.PAUSE = 0.2


def load_config(path: Path) -> dict[str, Any]:
    with path.open("r", encoding="utf-8") as handle:
        return json.load(handle)


def parse_daily_time(value: str) -> tuple[int, int]:
    hour_text, minute_text = value.split(":", maxsplit=1)
    hour = int(hour_text)
    minute = int(minute_text)
    if not (0 <= hour <= 23 and 0 <= minute <= 59):
        raise ValueError(f"Invalid daily_time: {value}")
    return hour, minute


def seconds_until_next_run(hour: int, minute: int) -> float:
    now = dt.datetime.now()
    target = now.replace(hour=hour, minute=minute, second=0, microsecond=0)
    if target <= now:
        target += dt.timedelta(days=1)
    return (target - now).total_seconds()


def wait_for_daily_time(config: dict[str, Any]) -> None:
    daily_time = config.get("daily_time")
    if not daily_time:
        return
    hour, minute = parse_daily_time(daily_time)
    seconds = seconds_until_next_run(hour, minute)
    target = dt.datetime.now() + dt.timedelta(seconds=seconds)
    print(f"[wait] Next run at {target:%Y-%m-%d %H:%M:%S}")
    while seconds > 0:
        sleep_chunk = min(seconds, 30)
        time.sleep(sleep_chunk)
        seconds -= sleep_chunk


def launch_target(config: dict[str, Any]) -> None:
    launch = config.get("launch", {})
    mode = launch.get("mode", "none")
    after_launch_seconds = float(launch.get("after_launch_seconds", 0))

    if mode == "none":
        print("[launch] Skipping launch")
    elif mode == "command":
        command = launch.get("command")
        if not command:
            raise ValueError("launch.command is required when launch.mode is 'command'")
        print(f"[launch] Running command: {command}")
        subprocess.Popen(command)
    elif mode == "steam_uri":
        steam_uri = launch.get("steam_uri")
        if not steam_uri:
            raise ValueError("launch.steam_uri is required when launch.mode is 'steam_uri'")
        print(f"[launch] Opening Steam URI: {steam_uri}")
        if sys.platform == "darwin":
            subprocess.Popen(["open", steam_uri])
        elif sys.platform.startswith("win"):
            subprocess.Popen(["cmd", "/c", "start", "", steam_uri], shell=False)
        else:
            subprocess.Popen(["xdg-open", steam_uri])
    else:
        raise ValueError(f"Unsupported launch mode: {mode}")

    if after_launch_seconds > 0:
        print(f"[launch] Waiting {after_launch_seconds:.1f}s for app startup")
        time.sleep(after_launch_seconds)


def supports_confidence_matching() -> bool:
    try:
        import cv2  # noqa: F401
    except ImportError:
        return False
    return True


def locate_center(
    image_path: Path,
    confidence: float,
    grayscale: bool,
    region: tuple[int, int, int, int] | None,
) -> Any:
    kwargs: dict[str, Any] = {
        "grayscale": grayscale,
    }
    if region is not None:
        kwargs["region"] = region
    if supports_confidence_matching():
        kwargs["confidence"] = confidence
    return pyautogui.locateCenterOnScreen(str(image_path), **kwargs)


def wait_for_image(
    image_path: Path,
    *,
    timeout_seconds: float,
    confidence: float,
    grayscale: bool,
    retry_interval_seconds: float,
    region: tuple[int, int, int, int] | None,
) -> Any:
    deadline = time.time() + timeout_seconds
    while time.time() <= deadline:
        point = locate_center(image_path, confidence, grayscale, region)
        if point is not None:
            return point
        time.sleep(retry_interval_seconds)
    return None


def as_region(value: Iterable[int] | None) -> tuple[int, int, int, int] | None:
    if value is None:
        return None
    left, top, width, height = value
    return int(left), int(top), int(width), int(height)


def click_point(point: Any, step: dict[str, Any], dry_run: bool) -> None:
    offset = step.get("center_offset", [0, 0])
    target_x = int(point.x + int(offset[0]))
    target_y = int(point.y + int(offset[1]))
    clicks = int(step.get("clicks", 1))
    button = step.get("button", "left")
    move_duration = float(step.get("move_duration_seconds", 0.15))

    print(f"[click] ({target_x}, {target_y}) button={button} clicks={clicks}")
    if dry_run:
        return

    pyautogui.moveTo(target_x, target_y, duration=move_duration)
    pyautogui.click(x=target_x, y=target_y, clicks=clicks, interval=0.15, button=button)


def run_step(
    step: dict[str, Any],
    *,
    templates_dir: Path,
    default_confidence: float,
    grayscale: bool,
    retry_interval_seconds: float,
    dry_run: bool,
) -> bool:
    step_type = step.get("type", "click_template")
    name = step.get("name", step_type)
    print(f"[step] {name}")

    if step_type == "sleep":
        seconds = float(step.get("seconds", 1))
        print(f"[sleep] {seconds:.1f}s")
        if not dry_run:
            time.sleep(seconds)
        return True

    template_name = step.get("template")
    if not template_name:
        raise ValueError(f"Step '{name}' is missing template")

    image_path = templates_dir / template_name
    if not image_path.exists():
        raise FileNotFoundError(f"Template not found: {image_path}")

    timeout_seconds = float(step.get("timeout_seconds", 30))
    confidence = float(step.get("confidence", default_confidence))
    region = as_region(step.get("region"))

    point = wait_for_image(
        image_path,
        timeout_seconds=timeout_seconds,
        confidence=confidence,
        grayscale=grayscale,
        retry_interval_seconds=retry_interval_seconds,
        region=region,
    )

    if point is None:
        if step.get("optional", False):
            print(f"[skip] Optional step not found: {template_name}")
            return True
        print(f"[error] Timed out waiting for {template_name}")
        return False

    print(f"[match] Found {template_name} at ({point.x}, {point.y})")
    click_point(point, step, dry_run=dry_run)

    delay_after_seconds = float(step.get("delay_after_seconds", 0))
    if delay_after_seconds > 0:
        print(f"[delay] {delay_after_seconds:.1f}s")
        if not dry_run:
            time.sleep(delay_after_seconds)
    return True


def run_flow(config: dict[str, Any], dry_run: bool) -> int:
    matching = config.get("matching", {})
    default_confidence = float(matching.get("default_confidence", 0.9))
    grayscale = bool(matching.get("grayscale", True))
    retry_interval_seconds = float(matching.get("retry_interval_seconds", 1.0))
    templates_dir = ROOT / "templates"

    if not supports_confidence_matching():
        print("[warn] OpenCV is not installed. Confidence matching is disabled.")

    launch_target(config)

    for index, step in enumerate(config.get("steps", []), start=1):
        print(f"[flow] Step {index}/{len(config.get('steps', []))}")
        success = run_step(
            step,
            templates_dir=templates_dir,
            default_confidence=default_confidence,
            grayscale=grayscale,
            retry_interval_seconds=retry_interval_seconds,
            dry_run=dry_run,
        )
        if not success:
            return 1
    return 0


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Run a screenshot-driven King's Call daily automation flow.")
    parser.add_argument("--config", type=Path, default=DEFAULT_CONFIG, help="Path to config JSON file")
    parser.add_argument("--run-now", action="store_true", help="Run immediately instead of waiting for daily_time")
    parser.add_argument("--dry-run", action="store_true", help="Find images but do not click")
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    config = load_config(args.config)

    if not args.run_now:
        wait_for_daily_time(config)

    try:
        return run_flow(config, dry_run=args.dry_run)
    except pyautogui.FailSafeException:
        print("[abort] Mouse moved to a screen corner. PyAutoGUI failsafe triggered.")
        return 130
    except KeyboardInterrupt:
        print("[abort] Interrupted by user.")
        return 130


if __name__ == "__main__":
    raise SystemExit(main())
