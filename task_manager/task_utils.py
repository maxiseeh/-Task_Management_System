from datetime import datetime
# Import the validation functions
from .validation import validate_task_title, validate_task_description, validate_due_date

# List to store all tasks
tasks = []

# Function to add a new task
def add_task(title, description, due_date):
    # Validate the inputs first
    good_title = validate_task_title(title)
    good_description = validate_task_description(description)
    good_date = validate_due_date(due_date)
    
    # Create a new task dictionary
    new_task = {
        "title": good_title,
        "description": good_description,
        "due_date": good_date,
        "completed": False
    }
    # Add task to the list
    tasks.append(new_task)
    print("Task added successfully!")
    
# Function to mark a task as done
def mark_task_as_complete(index, task_list=None):
    if task_list is None:
        task_list = tasks
    # Check if index is valid
    if index >= 0 and index < len(task_list):
        task_list[index]["completed"] = True
        print("Task marked as complete!")
    else:
        print("Invalid task index")
    
# Function to show tasks that are not done yet
def view_pending_tasks(task_list=None):
    if task_list is None:
        task_list = tasks
    # Find tasks that are not completed
    pending_tasks = []
    for task in task_list:
        if not task["completed"]:
            pending_tasks.append(task)
    
    # If no pending tasks
    if len(pending_tasks) == 0:
        print("No pending tasks!")
        return
    
    # Show pending tasks
    print("\nPending Tasks:")
    for i in range(len(pending_tasks)):
        task = pending_tasks[i]
        print(f"{i + 1}. {task['title']} - Due: {task['due_date']}")
        print(f"   Description: {task['description']}")

# Function to calculate how much work is done
def calculate_progress(task_list=None):
    if task_list is None:
        task_list = tasks
    # If no tasks, progress is 0
    if len(task_list) == 0:
        progress = 0.0
    else:
        # Count completed tasks
        completed_count = 0
        for task in task_list:
            if task["completed"]:
                completed_count = completed_count + 1
        # Calculate percentage
        progress = (completed_count / len(task_list)) * 100
    return progress