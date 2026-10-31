TASKS = []

def add_task(title):
    task = {"title": title, "done": False}
    TASKS.append(task)
    return task

def list_tasks():
    return TASKS
