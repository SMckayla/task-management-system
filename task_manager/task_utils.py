from datetime import datetime
from task_manager.validation import validate_task_title, validate_task_description, validate_due_date

# Define tasks list
tasks = []

# Implement add_task function
def add_task(title, description, due_date):
    if not validate_task_title(title):
        print("Error: Invalid task title.")
        return False
    if not validate_task_description(description):
        print("Error: Invalid task description.")
        return False
    if not validate_due_date(due_date):
        print("Error: Invalid due date format. Please use YYYY-MM-DD.")
        return False

    task = {
        "title": title,
        "description": description,
        "due_date": due_date,
        "completed": False
    }
    tasks.append(task)
    print("Task added successfully!")
    return True
    
# Implement mark_task_as_complete function
def mark_task_as_complete(index, tasks=tasks):
    try:
        if 0 <= index < len(tasks):
            tasks[index]["completed"] = True
            print("Task marked as complete!")
            return True
        else:
            print("Error: Task number out of range.")
            return False
    except (ValueError, TypeError):
        print("Error: Invalid task index.")
        return False
    
# Implement view_pending_tasks function
def view_pending_tasks(tasks=tasks):
    pending_tasks = [t for t in tasks if not t.get("completed", False)]
    if not pending_tasks:
        print("No pending tasks found.")
    else:
        for i, task in enumerate(tasks):
            if not task.get("completed", False):
                print(f"{i + 1}. Title: {task['title']} | Description: {task['description']} | Due Date: {task['due_date']} | Status: Pending")
    return pending_tasks

# Implement calculate_progress function
def calculate_progress(tasks=tasks):
    if not tasks:
        progress = 0.0
        print("Progress: 0.0% (0/0 tasks completed)")
    else:
        completed_count = sum(1 for t in tasks if t.get("completed", False))
        progress = (completed_count / len(tasks)) * 100
        print(f"Progress: {progress:.2f}% ({completed_count}/{len(tasks)} tasks completed)")
    return progress