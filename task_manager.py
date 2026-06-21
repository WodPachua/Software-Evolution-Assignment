"""Simple command-line Task Manager."""
import json
import os

DATA_FILE = "tasks.json"


def load_tasks():
    if not os.path.exists(DATA_FILE):
        return []
    with open(DATA_FILE) as f:
        return json.load(f)


def save_tasks(tasks):
    with open(DATA_FILE, "w") as f:
        json.dump(tasks, f, indent=2)


def main():
    tasks = load_tasks()
    print(f"Loaded {len(tasks)} task(s)")


if __name__ == "__main__":
    main()
