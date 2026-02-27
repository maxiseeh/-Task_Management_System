# Import functions from task_manager package
from task_manager.task_utils import add_task, mark_task_as_complete, view_pending_tasks, calculate_progress, tasks

# Main function that runs the program
def main():
    # Keep running until user chooses to exit
    while True:
        # Show menu options
        print("\nTask Management System")
        print("1. Add Task")
        print("2. Mark Task as Complete")
        print("3. View Pending Tasks")
        print("4. View Progress")
        print("5. Exit")
        choice = input("Enter your choice (1-5): ")

        # Option 1: Add a new task
        if choice == "1":
            try:
                # Get task details from user
                title = input("Enter task title: ")
                description = input("Enter task description: ")
                due_date = input("Enter due date (YYYY-MM-DD): ")
                # Try to add the task
                add_task(title, description, due_date)
            except ValueError as e:
                # Show error if something went wrong
                print(f"Error: {e}")
        
        # Option 2: Mark task as complete
        elif choice == "2":
            # Check if there are any tasks
            if len(tasks) == 0:
                print("No tasks available!")
            else:
                # Show all tasks
                print("\nAll Tasks:")
                for i in range(len(tasks)):
                    task = tasks[i]
                    # Show checkmark if completed, X if not
                    if task["completed"]:
                        status = "✓"
                    else:
                        status = "✗"
                    print(f"{i + 1}. [{status}] {task['title']}")
                
                try:
                    # Get task number from user
                    task_num = input("Enter task number to mark as complete: ")
                    index = int(task_num) - 1  # Convert to array index
                    mark_task_as_complete(index)
                except:
                    print("Invalid task number")
        
        # Option 3: View pending tasks
        elif choice == "3":
            view_pending_tasks()
        
        # Option 4: Show progress
        elif choice == "4":
            progress = calculate_progress()
            print(f"\nProgress: {progress:.1f}% complete")
            print(f"Total tasks: {len(tasks)}")
            
            # Count completed tasks
            completed = 0
            for task in tasks:
                if task["completed"]:
                    completed = completed + 1
            
            print(f"Completed: {completed}")
            print(f"Pending: {len(tasks) - completed}")
        
        # Option 5: Exit program
        elif choice == "5":
            print("Exiting the program...")
            break
        
        # Invalid choice
        else:
            print("Invalid choice. Please try again.")

# Run the program
if __name__ == "__main__":
    main()
