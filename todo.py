# todo.py - Persistent To-Do List (Console-based)

TASK_FILE = "tasks.txt"

def load_tasks():
    try:
        with open(TASK_FILE, "r") as f:
            return [line.strip() for line in f]
    except FileNotFoundError:
        return []

def save_tasks(tasks):
    with open(TASK_FILE, "w") as f:
        for t in tasks:
            f.write(t + "\n")

tasks = load_tasks()

while True:
    print("\n--- To-Do List ---")
    print("1. View tasks")
    print("2. Add task")
    print("3. Remove task")
    print("4. Exit")

    choice = input("Choose (1-4): ")

    if choice == "1":
        if not tasks:
            print("No tasks yet.")
        else:
            for i, t in enumerate(tasks, 1):
                print(f"{i}. {t}")

    elif choice == "2":
        task = input("Enter task: ")
        tasks.append(task)
        save_tasks(tasks)
        print(f"Task #{len(tasks)} added: {task}")

    elif choice == "3":
        if not tasks:
            print("No tasks to remove.")
        else:
            for i, t in enumerate(tasks, 1):
                print(f"{i}. {t}")
            try:
                num = int(input("Enter task number to remove: "))
                if 1 <= num <= len(tasks):
                    removed = tasks.pop(num - 1)
                    save_tasks(tasks)
                    print(f"Removed: {removed}")
                else:
                    print("Invalid number.")
            except ValueError:
                print("Please enter a valid number.")

    elif choice == "4":
        save_tasks(tasks)
        print("✅ Goodbye! All tasks saved to tasks.txt.")
        break

    else:
        print("Invalid choice.")
