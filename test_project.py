import pytest
from project import add_task, view_tasks, remove_task, load_tasks, save_tasks , TASK_FILE 

# Fixture to create a temporary tasks file
@pytest.fixture
def temp_task_file(tmpdir):
    # print("Im here ")
    file = tmpdir.join("temp_tasks.json")
    global TASK_FILE
    original_task_file = TASK_FILE
    # print("file name "+original_task_file)
    TASK_FILE = str(file)  # Override TASK_FILE with temp file path
    # print("override file name "+TASK_FILE)
    yield
    TASK_FILE = original_task_file  # Restore original TASK_FILE after tests
    # print("restore file name "+TASK_FILE)

def test_add_task(temp_task_file):
    save_tasks([])  # Clear existing tasks before testing
    task = add_task("Test task", "2024-12-01", "low")
    tasks = load_tasks()
    assert len(tasks) == 1
    assert tasks[0] == task

def test_view_tasks(temp_task_file):
    save_tasks([])  # Clear existing tasks before testing
    add_task("Task 1", "2024-12-01", "low")
    add_task("Task 2", "2024-12-02", "medium")
    add_task("Task 3", "2024-12-03", "high")

    tasks = view_tasks(filter={'priority': 'high'})
    assert len(tasks) == 1
    assert tasks[0]['description'] == "Task 3"

def test_remove_task(temp_task_file):
    save_tasks([])  # Clear existing tasks before testing
    add_task("Task to remove", "2024-12-04", "medium")
    task_id = load_tasks()[0]['id']
    remove_task(task_id)
    tasks = load_tasks()
    assert len(tasks) == 0

def test_add_multiple_tasks(temp_task_file):
    save_tasks([])  # Clear existing tasks before testing
    add_task("Task 1", "2024-12-01", "low")
    add_task("Task 2", "2024-12-02", "medium")
    add_task("Task 3", "2024-12-03", "high")
    tasks = load_tasks()
    assert len(tasks) == 3

def test_view_tasks_by_due_date(temp_task_file):
    save_tasks([])  # Clear existing tasks before testing
    add_task("Task A", "2024-12-01", "medium")
    add_task("Task B", "2024-12-01", "low")
    add_task("Task C", "2024-12-02", "high")

    tasks = view_tasks(filter={'due_date': '2024-12-01'})
    assert len(tasks) == 2
    assert all(task['due_date'] == '2024-12-01' for task in tasks)

def test_remove_non_existent_task(temp_task_file):
    save_tasks([])  # Clear existing tasks before testing
    add_task("Task X", "2024-12-01", "medium")
    tasks_before = load_tasks()
    remove_task(999)  # Removing a non-existent task
    tasks_after = load_tasks()
    assert tasks_before == tasks_after  # No change in tasks

def test_priority_case_insensitive_filter(temp_task_file):
    save_tasks([])  # Clear existing tasks before testing
    add_task("Important Task", "2024-12-05", "High")
    add_task("Not So Important Task", "2024-12-06", "Low")

    # Check if priority filter works case insensitively
    tasks = view_tasks(filter={'priority': 'HIGH'})
    assert len(tasks) == 1
    assert tasks[0]['description'] == "Important Task"

def test_remove_task_updates_ids(temp_task_file):
    save_tasks([])  # Clear existing tasks before testing
    task1 = add_task("Task 1", "2024-12-01", "low")
    task2 = add_task("Task 2", "2024-12-02", "medium")
    
    # Remove first task
    remove_task(task1['id'])
    tasks = load_tasks()
    
    assert len(tasks) == 1
    assert tasks[0]['id'] == task2['id']  # Ensure remaining task has the correct ID

def test_task_persistence(temp_task_file):
    save_tasks([])  # Clear existing tasks before testing
    add_task("Persistent Task", "2024-12-10", "medium")
    
    # Simulate program restart by reloading tasks
    tasks_after_reload = load_tasks()
    assert len(tasks_after_reload) == 1
    assert tasks_after_reload[0]['description'] == "Persistent Task"

def test_empty_task_list(temp_task_file):
    save_tasks([])  # Ensure empty task list
    tasks = view_tasks()
    assert len(tasks) == 0  # No tasks should be present

def test_task_with_same_due_date_and_priority(temp_task_file):
    save_tasks([])  # Clear existing tasks before testing
    add_task("Task 1", "2024-12-12", "high")
    add_task("Task 2", "2024-12-12", "high")
    tasks = view_tasks(filter={'priority': 'high', 'due_date': '2024-12-12'})
    assert len(tasks) == 2
