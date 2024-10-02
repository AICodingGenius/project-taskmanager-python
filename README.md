
# Todo List Manager Project

#### Video Demo: [Link to Video](https://youtu.be/n5WrlCtDvek)

#### Description:

This project is a simple task management tool that allows users to add, view, and remove tasks. It includes features for task visualization by priority and provides testing using `pytest`.

## Table of Contents

1. [Setup](#setup)
2. [Usage](#usage)
   - [Interactive Task Manager](#interactive-task-manager)
3. [Running the Tests](#running-the-tests)
4. [Visualizing Tasks](#visualizing-tasks)
5. [Images and Screenshots](#images-and-screenshots)
6. [License](#license)

---

## Setup

To set up and run this project, follow these steps:

1. **Clone the Repository**

   ```bash
   git clone https://github.com/AICodingGenius/project-todolist-python.git
   cd todo-list-manager
   ```

2. **Install Dependencies**

   Make sure you have `Python 3` and `pip` installed. You can install the required packages using the `requirements.txt` file:

   ```bash
   pip install -r requirements.txt
   ```

3. **Check Project Structure**

   The project directory should have the following structure:

   ```
   todo-list-manager/
   ├── project.py           # Main source code for the task manager
   ├── test_project.py      # Test file using pytest
   ├── requirements.txt     # List of dependencies
   ├── mytasks.json         # JSON file storing tasks
   └── README.md            # This file
   ```

---

## Usage

### Interactive Task Manager

An interactive command-line interface is provided to manage tasks without manually writing code. Run the following command to start the task manager:

```bash
python project.py
```

### Options Available:

1. **Add a Task**: Enter the description, due date (format `YYYY-MM-DD`), and priority (high, medium, low).
2. **View All Tasks**: Displays all tasks currently in the JSON file.
3. **View Tasks by Priority**: Filter tasks based on priority level.
4. **Remove a Task**: Delete a task by specifying its ID.
5. **Visualize Tasks by Priority**: Displays a bar chart of tasks categorized by priority.
6. **Pretty Print Tasks**: Outputs the JSON representation of tasks in a readable format.
7. **Exit**: Exit the interactive interface.

---

## Running the Tests

This project uses `pytest` for testing. All tests are contained in the `test_project.py` file.

### 1. Run All Tests

   To run all tests, execute:

   ```bash
   pytest -v
   ```

### 2. View Output Without Capturing

   To see print statements and other output during testing, use:

   ```bash
   pytest -v --capture=no
   ```

---

## Visualizing Tasks

The project includes a function to visualize tasks based on priority. To visualize tasks:

```python
from project import visualize_tasks_by_priority

visualize_tasks_by_priority()
```

This will generate a bar chart showing the count of tasks for each priority (e.g., high, medium, low).

---

## Images and Screenshots

Below are some images and screenshots to illustrate the different functionalities:

### Task Visualization
![Task Visualization](images/task_visualization.png)

### Running Tests
![Running Tests](images/running_tests.png)

---

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
