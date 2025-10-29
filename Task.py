tasks = []  # A list to store tasks

def add_task(task):
    tasks.append(task)
    print(f"Task '{task}' added!")

def view_tasks():
    if not tasks:
        print("No tasks available.")
    else:
        print("Your tasks:")
        for index, task in enumerate(tasks, 1):
            print(f"{index}. {task}")

def delete_task(task_number):
    if 1 <= task_number <= len(tasks):
        removed_task = tasks.pop(task_number - 1)
        print(f"Task '{removed_task}' deleted successfully!")
    else:
        print("Invalid task number.")

while True:
    print("\n1. Add Task\n2. View Tasks\n3. Delete Task\n4. Exit")
    choice = input("Choose an option: ")

    if choice == "1":
        task = input("Enter task: ")
        add_task(task)
    elif choice == "2":
        view_tasks()
    elif choice == "3":
        view_tasks()
        try:
            task_num = int(input("Enter task number to delete: "))
            delete_task(task_num)
        except ValueError:
            print("Invalid input. Please enter a number.")
    elif choice == "4":
        print("Goodbye!")
        break
    else:
        print("Invalid choice, try again.")