# Main function
def main():
    # Infinite loop to keep showing the menu until user choose to exit
    while True:
        # Display the menu options
        print("\nTo-Do List Menu:")
        print("1. Add Task")
        print("2. Show Tasks")
        print("3. Remove Task")
        print("4. Exit")

        # Get user's choice from the menu
        choice = input("Enter your choice: ")

        match choice:
            # Add a new task
            case "1":
                task = input("Enter task: ")
                add_task(task)  # Call the add_task()

            # Display all current tasks
            case "2":
                show_tasks()  # Call the show_tasks() function

            # Remove a specific task by number
            case "3":
                try:
                    # Convert the user's input to an integer
                    task_number = int(input("Enter task number to remove: ")) - 1
                    remove_task(task_number)
