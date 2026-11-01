TASKS = []


def add_task(title):
    task = {"title": title.strip(), "done": False}
    TASKS.append(task)
    return task


def list_tasks(only_done=False, sort_by_title=False):
    tasks = TASKS
    if only_done:
        tasks = [task for task in tasks if task.get("done")]
    if sort_by_title:
        tasks = sorted(tasks, key=lambda task: task["title"])
    return tasks