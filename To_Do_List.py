tasks = []

def listTask():
    if not tasks:
        print("There are no tasks left for you to do, Good Job!")
    else:
        print("Here are your tasks:")
        for index, task in enumerate(tasks, start=1):
            print(f" Task number {index}: {task}")

def addTask():
    task = input("Enter the task you want to add: ").strip()
    if task:
        tasks.append(task)
        print(f"Task '{task}' added successfully!")
    else:
        print("Task cannot be empty. Try again.")

def deleteTask():
    if not tasks:
        print("There are no tasks to delete.")
        return
    
    listTask()
    try:
        task_number = int(input("Enter the task number you want to delete: "))
        if 1 <= task_number <= len(tasks):
            removed_task = tasks.pop(task_number - 1)
            print(f"Task '{removed_task}' deleted successfully!")
        else:
            print("Invalid task number. Please try again.")
    except ValueError:
        print("Please enter a valid number.")

def main():
    while True:
        print("\n")
        print("________________________________")
        print("\n")
        print("Hi, Welcome to my To-Do List application! ;) ")
        print(" Please select what you want to do:")
        print("1. List out all the Tasks")
        print("2. Add a new Task")
        print("3. Delete an existing Task")
        print("4. Quit the Application")

        try:
            choice = int(input("Your choice here -> "))
        except ValueError:
            print("Invalid input! Please enter a number between 1 and 4.")
            continue

        if choice == 1:
            listTask()
        elif choice == 2:
            addTask()
        elif choice == 3:
            deleteTask()
        elif choice == 4:
            print("Thanks for using the To-Do app! Goodbye :)")
            break
        else:
            print("Please input a valid choice.")

if __name__ == "__main__":
    main()
