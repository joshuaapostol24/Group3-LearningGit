# toDoApp.py

tasks = []

def add_task(task):
  if task.strip() == "":
     print("Cannot add an empty task!")
  else:
    tasks.append(task)
    print("Task added!")

def show_tasks():
    if not tasks:
     print("No tasks yet.")
    else:
        print("\nYour Tasks:")
        for i, task in enumerate(tasks, start=1):
          print(f"{i}. {task}")

def remove_task(task_number):
    if 0 <= task_number < len(tasks):
      toRemove = tasks[task_number]
      confirm = input(f"Are you sure you want to remove '{toRemove}'? (y/n): ").lower()
      if confirm == "y":
        removed = tasks.pop(task_number)
        print(f"Task '{removed}' removed!")
      else:
         print(f"Task was not removed.")
    else:
      print("Invalid task number.")