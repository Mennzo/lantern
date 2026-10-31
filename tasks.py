TASKS = []

def add_task(title):
    task = {"title": title}
    TASKS.append(task)
    return task

def list_tasks():
    return TASKS
