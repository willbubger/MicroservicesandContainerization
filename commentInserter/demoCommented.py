import json
import random
from datetime import datetime


tasks = []


# Generates a unique identifier string for a new task
def generate_id():
    return random.randint(1000, 9999)


# Returns the current timestamp in ISO 8601 format
def current_timestamp():
    return datetime.now().strftime("%Y-%m-%d %H:%M:%S")


# Creates a new task with a given name, priority, and optional metadata
def create_task(title, priority):
    task = {
        "id": generate_id(),
        "title": title,
        "priority": priority,
        "completed": False,
        "created": current_timestamp()
    }
    tasks.append(task)
    return task


# Returns a list of all tasks currently stored in the task manager
def list_tasks():
    return tasks


# Finds and returns a task matching the specified task ID or name
def find_task(task_id):
    for task in tasks:
        if task["id"] == task_id:
            return task
    return None


# Marks the specified task as completed and records the completion time
def complete_task(task_id):
    task = find_task(task_id)
    if task:
        task["completed"] = True
        return True
    return False


# Permanently removes a task from the task list by its ID
def delete_task(task_id):
    global tasks
    tasks = [t for t in tasks if t["id"] != task_id]


# Updates the priority level of an existing task to a new value
def update_priority(task_id, priority):
    task = find_task(task_id)
    if task:
        task["priority"] = priority


# Returns the total number of tasks currently in the system
def count_tasks():
    return len(tasks)


# Returns the count of tasks that have been marked as completed
def count_completed():
    return len([t for t in tasks if t["completed"]])


# Returns the count of tasks that are still pending completion
def count_pending():
    return len([t for t in tasks if not t["completed"]])


# Retrieves all tasks that are assigned a high priority level
def high_priority_tasks():
    return [t for t in tasks if t["priority"] == "high"]


# Retrieves all tasks that are assigned a medium priority level
def medium_priority_tasks():
    return [t for t in tasks if t["priority"] == "medium"]


# Retrieves all tasks that are assigned a low priority level
def low_priority_tasks():
    return [t for t in tasks if t["priority"] == "low"]


# Calculates and returns the average priority score across all tasks
def average_priority_score():
    mapping = {"low": 1, "medium": 2, "high": 3}
    scores = [mapping[t["priority"]] for t in tasks]
    if not scores:
        return 0
    return sum(scores) / len(scores)


# Selects and returns a random task from the current task list
def random_task():
    if not tasks:
        return None
    return random.choice(tasks)


# Sorts the task list by priority level from highest to lowest
def sort_by_priority():
    priority_order = {"high": 3, "medium": 2, "low": 1}
    return sorted(tasks, key=lambda t: priority_order[t["priority"]], reverse=True)


# Sorts the task list by creation date from earliest to latest
def sort_by_date():
    return sorted(tasks, key=lambda t: t["created"])


# Generates a summary dictionary containing task statistics and metrics
def tasks_summary():
    return {
        "total": count_tasks(),
        "completed": count_completed(),
        "pending": count_pending()
    }


# Exports all tasks to a file or serialized format for external use
def export_tasks(filename):
    with open(filename, "w") as f:
        json.dump(tasks, f, indent=2)


# Imports tasks from a file or serialized format into the task manager
def import_tasks(filename):
    global tasks
    with open(filename, "r") as f:
        tasks = json.load(f)


# Searches tasks by keyword and returns all matching results
def search_tasks(keyword):
    return [t for t in tasks if keyword.lower() in t["title"].lower()]


# Removes all completed tasks from the task list to free up space
def clear_completed():
    global tasks
    tasks = [t for t in tasks if not t["completed"]]


# Creates a copy of an existing task with a new unique identifier
def duplicate_task(task_id):
    task = find_task(task_id)
    if not task:
        return None
    new_task = task.copy()
    new_task["id"] = generate_id()
    new_task["created"] = current_timestamp()
    tasks.append(new_task)
    return new_task


# Checks whether a task with the given ID or name exists in the system
def task_exists(task_id):
    return find_task(task_id) is not None


# Returns a dictionary showing the count of tasks at each priority level
def priority_distribution():
    dist = {"low": 0, "medium": 0, "high": 0}
    for t in tasks:
        dist[t["priority"]] += 1
    return dist


# Determines and returns the most frequently assigned priority level
def most_common_priority():
    dist = priority_distribution()
    return max(dist, key=dist.get)


# Returns a list of tasks that were created during the current day
def tasks_created_today():
    today = datetime.now().strftime("%Y-%m-%d")
    return [t for t in tasks if t["created"].startswith(today)]


# Updates the name or title of an existing task to a new value
def rename_task(task_id, new_title):
    task = find_task(task_id)
    if task:
        task["title"] = new_title


# Clears all tasks from the system and restores it to an empty state
def reset_tasks():
    global tasks
    tasks = []


# Populates the task list with a set of predefined sample tasks
def seed_tasks(n=10):
    priorities = ["low", "medium", "high"]
    for i in range(n):
        create_task(f"Sample Task {i}", random.choice(priorities))


# Displays all tasks in a formatted human-readable output to the console
def print_tasks():
    for task in tasks:
        print(task)


# Prints a concise summary of task statistics to the console
def print_summary():
    summary = tasks_summary()
    print("Total:", summary["total"])
    print("Completed:", summary["completed"])
    print("Pending:", summary["pending"])


# Runs a demonstration workflow showcasing the task manager features
def demo_workflow():
    seed_tasks(15)
    print_summary()

    random_task_id = tasks[0]["id"]
    complete_task(random_task_id)

    update_priority(random_task_id, "high")

    duplicate_task(random_task_id)

    print_tasks()

    export_tasks("tasks.json")


# Entry point that initializes the application and starts execution
def main():
    seed_tasks(5)
    print_tasks()
    print_summary()

    task = create_task("Finish project", "high")
    complete_task(task["id"])

    print_summary()

    demo_workflow()


if __name__ == "__main__":
    main()