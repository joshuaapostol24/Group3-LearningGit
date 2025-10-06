# toDoApp.py

tasks = []

def add_task(task):
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
     removed = tasks.pop(task_number)
      print(f"Task '{removed}' removed!")
    else:
     print("Invalid task number.")