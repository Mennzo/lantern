TASKS = []

def add_task(title):
    task = {"title": title.strip(), "done": False}
    TASKS.append(task)
    return task

def list_tasks(only_done=False):
    if only_done:
        return [t for t in TASKS if t.get("done")]
    return TASKS
