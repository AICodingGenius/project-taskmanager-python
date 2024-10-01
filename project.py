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
    return task

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
    plt.show()
def main():
    print("Adding tasks...")
    add_task("Test High Task", "2024-10-10", "high")
    add_task("Test Medium Task", "2024-10-05", "medium")
    add_task("Test Low Task", "2024-10-05", "low")
    
    print("\nAll tasks:")
    tasks = view_tasks()
    display_tasks(tasks)

    print("\nTasks with high priority:")
    high_priority_tasks = view_tasks(filter={'priority': 'high'})
    display_tasks(high_priority_tasks)

    print("\nTasks with medium priority:")
    medium_priority_tasks = view_tasks(filter={'priority': 'medium'})
    display_tasks(medium_priority_tasks)

    print("\nTasks with low priority:")
    low_priority_tasks = view_tasks(filter={'priority': 'low'})
    display_tasks(low_priority_tasks)

    print("\nPretty printing all tasks in the file:")
    pretty_print_tasks()

    print("\nRemoving task with ID 1")
    remove_task(1)

    print("\nTasks after deletion:")
    tasks = view_tasks()
    display_tasks(tasks)
    visualize_tasks_by_priority()

if __name__ == "__main__":
    main()
