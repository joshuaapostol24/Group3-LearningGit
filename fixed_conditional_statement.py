def main():
    while True:
        print("\nTo-Do List Menu:")
        print("1. Add Task")
        print("2. Show Tasks")
        print("3. Remove Task")
        print("4. Exit")

        choice = input("Enter your choice: ")

        match choice:
            case "1":
                task = input("Enter task: ")
                add_task(task)
            case "2":
                show_tasks()
            case "3":
                try:
                    task_number = int(input("Enter task number to remove: ")) - 1
                    remove_task(task_number)
                except ValueError:
                    print("Please enter a valid number.")
            case "4":
                print("Goodbye!")
                break
            case _:
                print("Wrong choice!")

main()
