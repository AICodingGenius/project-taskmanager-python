import json
from datetime import datetime
import matplotlib.pyplot as plt
from collections import Counter

TASK_FILE = 'mytasks.json'

# Function to add a task
def add_task(description, due_date, priority):
    task = {
        "id": generate_task_id(),
        "description": description,
        "due_date": due_date,
        "priority": priority
    }
    tasks = load_tasks()
    tasks.append(task)
    save_tasks(tasks)
    print(f"Task added: {task}")

# Function to view tasks with optional filtering
def view_tasks(filter=None):
    tasks = load_tasks()
    if filter:
        if 'priority' in filter:
            tasks = [task for task in tasks if task['priority'].lower() == filter['priority'].lower()]
        elif 'due_date' in filter:
            tasks = [task for task in tasks if task['due_date'] == filter['due_date']]
    return tasks

# Function to remove a task by ID
def remove_task(task_id):
    tasks = load_tasks()
    if any(task['id'] == task_id for task in tasks):
        tasks = [task for task in tasks if task['id'] != task_id]
        save_tasks(tasks)
        print(f"Task with ID {task_id} removed.")
    else:
        print(f"Task with ID {task_id} not found.")

# Helper function to generate a unique task ID
def generate_task_id():
    tasks = load_tasks()
    if tasks:
        return max(task['id'] for task in tasks) + 1
    return 1

# Load tasks from file
def load_tasks():
    try:
        with open(TASK_FILE, 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return []
    except json.JSONDecodeError:
        return []

# Save tasks to file
def save_tasks(tasks):
    with open(TASK_FILE, 'w') as file:
        json.dump(tasks, file, indent=4)

# Function to display tasks nicely
def display_tasks(tasks):
    if not tasks:
        print("No tasks found.")
    for task in tasks:
        print(f"ID: {task['id']}, Description: {task['description']}, Due Date: {task['due_date']}, Priority: {task['priority']}")

# Function to pretty print the task JSON file
def pretty_print_tasks():
    try:
        with open(TASK_FILE, 'r') as file:
            tasks = json.load(file)
        pretty_json = json.dumps(tasks, indent=4)
        print(pretty_json)
    except FileNotFoundError:
        print(f"The file {TASK_FILE} was not found.")
    except json.JSONDecodeError:
        print(f"The file {TASK_FILE} does not contain valid JSON.")

# Function to visualize tasks by priority
def visualize_tasks_by_priority():
    tasks = load_tasks()
    priorities = [task['priority'].lower() for task in tasks]  # Normalizing priority for consistent comparison
    priority_counts = Counter(priorities)

    # Define colors for each priority level
    priority_colors = {
        'high': 'red',
        'medium': 'orange',
        'low': 'green'
    }

    # Get colors for the bars based on priorities
    bar_colors = [priority_colors.get(priority, 'blue') for priority in priority_counts.keys()]

    # Plotting the data
    plt.figure(figsize=(8, 5))
    plt.bar(priority_counts.keys(), priority_counts.values(), color=bar_colors)
    plt.title('Tasks by Priority')
    plt.xlabel('Priority')
    plt.ylabel('Count')
    plt.show(block=False)

def main():
    print("Welcome to the Task Manager!")
    
    while True:
        print("\nPlease choose an option:")
        print("1. Add a task")
        print("2. View all tasks")
        print("3. View tasks by priority")
        print("4. Remove a task")
        print("5. Visualize tasks by priority")
        print("6. Pretty print tasks")
        print("7. Exit")
        
        choice = input("Enter your choice (1-7): ").strip()
        
        if choice == '1':
            description = input("Enter task description: ").strip()
            due_date = input("Enter task due date (YYYY-MM-DD): ").strip()
            priority = input("Enter task priority (high, medium, low): ").strip().lower()
            add_task(description, due_date, priority)
        
        elif choice == '2':
            tasks = view_tasks()
            print("\nAll tasks:")
            display_tasks(tasks)
        
        elif choice == '3':
            priority = input("Enter the priority to filter by (high, medium, low): ").strip().lower()
            tasks = view_tasks(filter={'priority': priority})
            print(f"\nTasks with priority '{priority}':")
            display_tasks(tasks)
        
        elif choice == '4':
            try:
                task_id = int(input("Enter the task ID to remove: ").strip())
                remove_task(task_id)
            except ValueError:
                print("Invalid ID. Please enter a number.")
        
        elif choice == '5':
            visualize_tasks_by_priority()
        
        elif choice == '6':
            pretty_print_tasks()
        
        elif choice == '7':
            print("Exiting Task Manager. Goodbye!")
            break
        
        else:
            print("Invalid choice. Please select a valid option.")

if __name__ == "__main__":
    main()
