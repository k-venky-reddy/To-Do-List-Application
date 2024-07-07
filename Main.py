import json
import datetime

TASKS_FILE = 'tasks.json'

def load_tasks():
    try:
        with open(TASKS_FILE, 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return []

def save_tasks(tasks):
    with open(TASKS_FILE, 'w') as file:
        json.dump(tasks, file, indent=4)

def add_task(tasks, title, priority, due_date):
    task = {
        'title': title,
        'priority': priority,
        'due_date': due_date,
        'completed': False
    }
    tasks.append(task)
    save_tasks(tasks)
    print("Task added successfully.")

def remove_task(tasks, index):
    if 0 <= index < len(tasks):
        del tasks[index]
        save_tasks(tasks)
        print("Task removed successfully.")
    else:
        print("Invalid task index.")

def mark_completed(tasks, index):
    if 0 <= index < len(tasks):
        tasks[index]['completed'] = True
        save_tasks(tasks)
        print("Task marked as completed.")
    else:
        print("Invalid task index.")

def list_tasks(tasks):
    if not tasks:
        print("No tasks found.")
    else:
        for idx, task in enumerate(tasks):
            status = 'Completed' if task['completed'] else 'Pending'
            print(f"{idx + 1}. {task['title']} - Priority: {task['priority']} - Due Date: {task['due_date']} - Status: {status}")

def get_user_input():
    print("\n1. Add Task")
    print("2. Remove Task")
    print("3. Mark Task as Completed")
    print("4. List Tasks")
    print("5. Exit")
    return input("Choose an option: ")

def main():
    tasks = load_tasks()
    while True:
        option = get_user_input()
        if option == '1':
            title = input("Enter task title: ")
            priority = input("Enter task priority (high/medium/low): ")
            due_date = input("Enter due date (YYYY-MM-DD): ")
            add_task(tasks, title, priority, due_date)
        elif option == '2':
            list_tasks(tasks)
            index = int(input("Enter the index of the task to remove: ")) - 1
            remove_task(tasks, index)
        elif option == '3':
            list_tasks(tasks)
            index = int(input("Enter the index of the task to mark as completed: ")) - 1
            mark_completed(tasks, index)
        elif option == '4':
            list_tasks(tasks)
        elif option == '5':
            break
        else:
            print("Invalid option. Please choose a valid option.")

if __name__ == "__main__":
    main()



