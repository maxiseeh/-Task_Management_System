from datetime import datetime

# Import validation functions
from task_manager.validation import validate_task_title, validate_task_description, validate_due_date

# Define tasks list
tasks = []

# Implement add_task function
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
    
# Implement mark_task_as_complete function
def mark_task_as_complete(index, tasks=tasks):
    # Check if index is valid
    if index >= 0 and index < len(tasks):
        tasks[index]["completed"] = True
        print("Task marked as complete!")
    else:
        print("Invalid task index")
    
# Implement view_pending_tasks function
def view_pending_tasks(tasks=tasks):
    # Find tasks that are not completed
    pending_tasks = []
    for task in tasks:
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

# Implement calculate_progress function
def calculate_progress(tasks=tasks):
    # If no tasks, progress is 0
    if len(tasks) == 0:
        progress = 0.0
    else:
        # Count completed tasks
        completed_count = 0
        for task in tasks:
            if task["completed"]:
                completed_count = completed_count + 1
        # Calculate percentage
        progress = (completed_count / len(tasks)) * 100.0
    return progress