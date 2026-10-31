TASKS = []

def add_task(title):
    task = {"title": title.strip()}
    TASKS.append(task)
    return task

def list_tasks():
    return TASKS
