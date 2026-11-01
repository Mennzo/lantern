TASKS = []

def add_task(title):
    task = {"title": title.strip(), "done": False}
    TASKS.append(task)
    return task

def list_tasks(sort_by_title=False):
    if sort_by_title:
        return sorted(TASKS, key=lambda task: task["title"])
    return TASKS