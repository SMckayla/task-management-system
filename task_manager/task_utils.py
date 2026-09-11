from datetime import datetime
from task_manager.validation import validate_task_title, validate_task_description, validate_due_date

tasks = []


def add_task(title, description, due_date):
    try:
        validate_task_title(title)
        validate_task_description(description)
        validate_due_date(due_date)
    except ValueError as e:
        print(f"Error: {e}")
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
    

def view_pending_tasks(tasks=tasks):
    pending_tasks = [t for t in tasks if not t.get("completed", False)]
    if not pending_tasks:
        print("No pending tasks found.")
    else:
        for i, task in enumerate(tasks):
            if not task.get("completed", False):
                print(f"{i + 1}. Title: {task['title']} | Description: {task['description']} | Due Date: {task['due_date']} | Status: Pending")
    return pending_tasks


def calculate_progress(tasks=tasks):
    if not tasks:
        return 0.0
    completed_count = sum(1 for t in tasks if t.get("completed", False))
    progress = (completed_count / len(tasks)) * 100
    return progress