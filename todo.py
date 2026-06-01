FILE_NAME = "tasks.txt"

# Load tasks from file
def load_tasks():
    try:
        with open(FILE_NAME, "r") as file:
            tasks = [line.strip() for line in file]
        return tasks
    except FileNotFoundError:
        return []

# Save tasks to file
def save_tasks(tasks):
    with open(FILE_NAME, "w") as file:
        for task in tasks:
            file.write(task + "\n")

# Main Program
tasks = load_tasks()

while True:
    print("\n========================")
    print("     TO-DO LIST APP")
    print("========================")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Remove Task")
    print("4. Exit")

    choice = input("Enter your choice: ")

    # Add Task
    if choice == "1":
        task = input("Enter task: ")

        if task.strip() == "":
            print("Task cannot be empty!")
        else:
            tasks.append(task)
            save_tasks(tasks)
            print("Task added successfully!")

    # View Tasks
    elif choice == "2":
        if len(tasks) == 0:
            print("No tasks available.")
        else:
            print("\nYour Tasks:")
            for index, task in enumerate(tasks, start=1):
                print(f"{index}. {task}")

    # Remove Task
    elif choice == "3":
        if len(tasks) == 0:
            print("No tasks to remove.")
        else:
            print("\nTasks:")
            for index, task in enumerate(tasks, start=1):
                print(f"{index}. {task}")

            try:
                task_number = int(input("Enter task number to remove: "))

                if 1 <= task_number <= len(tasks):
                    removed_task = tasks.pop(task_number - 1)
                    save_tasks(tasks)
                    print(f"Removed: {removed_task}")
                else:
                    print("Invalid task number.")

            except ValueError:
                print("Please enter a valid number.")

    # Exit
    elif choice == "4":
        print("Thank you for using To-Do List App!")
        break

    else:
        print("Invalid choice. Try again.")