from datetime import datetime

# Function to check if title is valid
def validate_task_title(title):
    # Check if title is empty
    if not title or not title.strip():
        raise ValueError("Title cannot be empty")
    # Check if title is too long
    if len(title.strip()) > 100:
        raise ValueError("Title cannot exceed 100 characters")
    return title.strip()
    
# Function to check if description is valid
def validate_task_description(description):
    # Check if description is empty
    if not description or not description.strip():
        raise ValueError("Description cannot be empty")
    # Check if description is too long
    if len(description.strip()) > 500:
        raise ValueError("Description cannot exceed 500 characters")
    return description.strip()
    
# Function to check if date is valid
def validate_due_date(due_date):
    try:
        # Try to convert string to date
        date_obj = datetime.strptime(due_date, "%Y-%m-%d")
        return due_date
    except ValueError as e:
        # If date format is wrong
        if "time data" in str(e):
            raise ValueError("Invalid date format. Use YYYY-MM-DD")
        raise e