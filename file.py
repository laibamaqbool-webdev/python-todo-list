# ============================================================
# Project 1: To-Do List Manager
# Developer: Laiba Maqbool
# DecodeLabs Industrial Training Program 2026
# ============================================================

import json
import os

# Store tasks in a list
my_tasks = []
next_id = 1

# File for saving tasks
DATA_FILE = "tasks_data.json"


def save_tasks():
    """Save tasks to JSON file."""
    with open(DATA_FILE, "w") as file:
        json.dump({"tasks": my_tasks, "next_id": next_id}, file, indent=4)


def load_tasks():
    """Load tasks from JSON file."""
    global my_tasks, next_id

    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, "r") as file:
            data = json.load(file)
            my_tasks = data.get("tasks", [])
            next_id = data.get("next_id", 1)


def add_task(task_name):
    """Add a new task."""
    global next_id

    task = {
        "id": next_id,
        "task": task_name,
        "done": False
    }

    my_tasks.append(task)
    next_id += 1
    save_tasks()

    return task


def view_tasks():
    """Display all tasks."""

    if not my_tasks:
        print("\nNo tasks available.\n")
        return

    print("\n" + "=" * 40)
    print("TO-DO LIST")
    print("=" * 40)

    for index, task in enumerate(my_tasks, start=1):
        status = "Completed" if task["done"] else "Pending"
        print(f"{index}. [{task['id']}] {task['task']} - {status}")

    print("=" * 40)


def mark_done(task_id):
    """Mark task as completed."""

    for task in my_tasks:
        if task["id"] == task_id:
            task["done"] = True
            save_tasks()
            return True

    return False


def delete_task(task_id):
    """Delete a task."""

    global my_tasks

    old_length = len(my_tasks)

    my_tasks = [task for task in my_tasks if task["id"] != task_id]

    if len(my_tasks) < old_length:
        save_tasks()
        return True

    return False


def show_menu():
    """Display menu."""

    print("\n" + "-" * 40)
    print("To-Do List Manager")
    print("-" * 40)
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Mark Task as Done")
    print("4. Delete Task")
    print("5. Exit")
    print("-" * 40)


def get_int_input(message):
    """Get valid integer input."""

    while True:
        try:
            return int(input(message))
        except ValueError:
            print("Please enter a valid number.")


def main():

    load_tasks()

    print("\nWelcome to To-Do List Manager\n")

    while True:

        show_menu()
        choice = get_int_input("Enter your choice (1-5): ")

        if choice == 1:

            task_name = input("Enter task description: ").strip()

            if task_name:
                task = add_task(task_name)
                print(f"Task added successfully. ID = {task['id']}")
            else:
                print("Task description cannot be empty.")

        elif choice == 2:
            view_tasks()

        elif choice == 3:

            view_tasks()
            task_id = get_int_input("Enter task ID: ")

            if mark_done(task_id):
                print("Task marked as completed.")
            else:
                print("Task not found.")

        elif choice == 4:

            view_tasks()
            task_id = get_int_input("Enter task ID: ")

            if delete_task(task_id):
                print("Task deleted successfully.")
            else:
                print("Task not found.")

        elif choice == 5:
            print("\nProgram Closed.\n")
            break

        else:
            print("Invalid choice. Please select between 1 and 5.")


if __name__ == "__main__":
    main()