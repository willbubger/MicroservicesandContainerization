import json
import random
from datetime import datetime


tasks = []


def generate_id():
    return random.randint(1000, 9999)


def current_timestamp():
    return datetime.now().strftime("%Y-%m-%d %H:%M:%S")


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


def list_tasks():
    return tasks


def find_task(task_id):
    for task in tasks:
        if task["id"] == task_id:
            return task
    return None


def complete_task(task_id):
    task = find_task(task_id)
    if task:
        task["completed"] = True
        return True
    return False


def delete_task(task_id):
    global tasks
    tasks = [t for t in tasks if t["id"] != task_id]


def update_priority(task_id, priority):
    task = find_task(task_id)
    if task:
        task["priority"] = priority


def count_tasks():
    return len(tasks)


def count_completed():
    return len([t for t in tasks if t["completed"]])


def count_pending():
    return len([t for t in tasks if not t["completed"]])


def high_priority_tasks():
    return [t for t in tasks if t["priority"] == "high"]


def medium_priority_tasks():
    return [t for t in tasks if t["priority"] == "medium"]


def low_priority_tasks():
    return [t for t in tasks if t["priority"] == "low"]


def average_priority_score():
    mapping = {"low": 1, "medium": 2, "high": 3}
    scores = [mapping[t["priority"]] for t in tasks]
    if not scores:
        return 0
    return sum(scores) / len(scores)


def random_task():
    if not tasks:
        return None
    return random.choice(tasks)


def sort_by_priority():
    priority_order = {"high": 3, "medium": 2, "low": 1}
    return sorted(tasks, key=lambda t: priority_order[t["priority"]], reverse=True)


def sort_by_date():
    return sorted(tasks, key=lambda t: t["created"])


def tasks_summary():
    return {
        "total": count_tasks(),
        "completed": count_completed(),
        "pending": count_pending()
    }


def export_tasks(filename):
    with open(filename, "w") as f:
        json.dump(tasks, f, indent=2)


def import_tasks(filename):
    global tasks
    with open(filename, "r") as f:
        tasks = json.load(f)


def search_tasks(keyword):
    return [t for t in tasks if keyword.lower() in t["title"].lower()]


def clear_completed():
    global tasks
    tasks = [t for t in tasks if not t["completed"]]


def duplicate_task(task_id):
    task = find_task(task_id)
    if not task:
        return None
    new_task = task.copy()
    new_task["id"] = generate_id()
    new_task["created"] = current_timestamp()
    tasks.append(new_task)
    return new_task


def task_exists(task_id):
    return find_task(task_id) is not None


def priority_distribution():
    dist = {"low": 0, "medium": 0, "high": 0}
    for t in tasks:
        dist[t["priority"]] += 1
    return dist


def most_common_priority():
    dist = priority_distribution()
    return max(dist, key=dist.get)


def tasks_created_today():
    today = datetime.now().strftime("%Y-%m-%d")
    return [t for t in tasks if t["created"].startswith(today)]


def rename_task(task_id, new_title):
    task = find_task(task_id)
    if task:
        task["title"] = new_title


def reset_tasks():
    global tasks
    tasks = []


def seed_tasks(n=10):
    priorities = ["low", "medium", "high"]
    for i in range(n):
        create_task(f"Sample Task {i}", random.choice(priorities))


def print_tasks():
    for task in tasks:
        print(task)


def print_summary():
    summary = tasks_summary()
    print("Total:", summary["total"])
    print("Completed:", summary["completed"])
    print("Pending:", summary["pending"])


def demo_workflow():
    seed_tasks(15)
    print_summary()

    random_task_id = tasks[0]["id"]
    complete_task(random_task_id)

    update_priority(random_task_id, "high")

    duplicate_task(random_task_id)

    print_tasks()

    export_tasks("tasks.json")


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