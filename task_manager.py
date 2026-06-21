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


def print_menu():
    print("Task Manager")
    print("1. Add task")
    print("2. List tasks")
    print("3. Exit")


def add_task(tasks, title):
    tasks.append({"title": title, "done": False})
    save_tasks(tasks)
    print(f"Added: {title}")


def list_tasks(tasks):
    if not tasks:
        print("No tasks yet.")
        return
    for i, t in enumerate(tasks, 1):
        status = "x" if t["done"] else " "
        print(f"{i}. [{status}] {t['title']}")


def main():
    tasks = load_tasks()
    while True:
        print_menu()
        choice = input("Choose an option: ").strip()
        if choice == "1":
            add_task(tasks, input("Task title: "))
        elif choice == "2":
            list_tasks(tasks)
        elif choice == "3":
            break
        else:
            print("Invalid option")


if __name__ == "__main__":
    main()
