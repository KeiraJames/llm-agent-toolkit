from modules.planners.planner import Planner
from modules.memory.memory import Memory

class PlanningAgent:
    """Agent that can store items in memory and manage a task list."""
    def __init__(self, name: str):
        self.name = name
        self.memory = Memory()
        self.planner = Planner()

    # ---- Memory actions ----
    def remember(self, item: str):
        self.memory.add(item)
        return f"Remembered: {item}"

    def recall_all(self):
        return self.memory.get_all()

    def forget_all(self):
        self.memory.clear()
        return "Memory cleared"

    # ---- Planning actions ----
    def add_task(self, task: str):
        self.planner.add_task(task)
        return f"Task added: {task}"

    def next_task(self):
        return self.planner.next_task()

    def peek_tasks(self):
        return self.planner.peek_tasks()
