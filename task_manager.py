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
    print("=" * 32)
    print("         TASK MANAGER")
    print("=" * 32)
    print("  [1] Add task")
    print("  [2] List tasks")
    print("  [3] Complete task")
    print("  [4] Delete task")
    print("  [5] Exit")
    print("=" * 32)


def add_task(tasks, title):
    title = title.strip()
    if not title:
        print("Task title cannot be empty.")
        return
    tasks.append({"title": title, "done": False})
    save_tasks(tasks)
    print(f"Added: {title}")


def list_tasks(tasks):
    if not tasks:
        print("No tasks yet.")
        return
    for i, t in enumerate(tasks, 1):
        icon = "[done]" if t["done"] else "[ todo ]"
        print(f"  {i:>2}. {icon}  {t['title']}")


def complete_task(tasks, index):
    tasks[index]["done"] = True
    save_tasks(tasks)
    print(f"Completed: {tasks[index]['title']}")


def delete_task(tasks, index):
    removed = tasks.pop(index)
    save_tasks(tasks)
    print(f"Deleted: {removed['title']}")


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
            complete_task(tasks, int(input("Task number: ")) - 1)
        elif choice == "4":
            delete_task(tasks, int(input("Task number: ")) - 1)
        elif choice == "5":
            break
        else:
            print("Invalid option")


if __name__ == "__main__":
    main()
