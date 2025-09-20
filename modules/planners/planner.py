class Planner:

    def __init__(self):
        self.tasks = []

    def add_task(self, task: str):
        self.tasks.append(task)

    def next_task(self):
        if self.tasks:
            return self.tasks.pop(0)
        return None

    def peek_tasks(self):
        return list(self.tasks)
    
