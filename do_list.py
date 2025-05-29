#to do list can help you to manage your tasks
#you can add, remove, list, update tasks
def to_do_list():
    tasks = []
#use while loop to keep the program running until user decides to exit
    print("Welcome to py_to_do_list")
    while True:
        print("\n1. Add task")
        print("2. Remove task")
        print("3. List tasks")
        print("4. Exit")
        choice = input("Please choose any option: ")
        if choice == "1":
            task = input("Enter your task to add: ")
            tasks.append(task)
            print(f"Task '{task}' added.")
        elif choice == "2":
            task = input("Enter task you want to remove: ")
            if task in tasks:
                tasks.remove(task)
                print(f"Task '{task}' removed.")
            else:
                print(f"{task} not found")
        elif choice == "3":
            print("Tasks: ")
            for t in tasks:
                print("- " + t)
        elif choice == "4":
            print("Exiting...")
            break
        else:
            print("Invalid choice")
if __name__ == "__main__":
    to_do_list()