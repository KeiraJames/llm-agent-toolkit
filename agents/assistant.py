# imports at the top
from modules.memory.memory import Memory
from modules.planners.planner import Planner
from modules.tools.shell_tools import run_command
from modules.tools.code_runner import run_python

class Assistant:
    #All-in-one agent: memory + planner + system ops + code runner.
    def __init__(self):
        self.memory = Memory()
        self.planner = Planner()
        self.run_command = run_command
        self.run_python = run_python

    # ---- Memory ----
    def remember(self, note: str):
        self.memory.add(note)
        return f"Remembered: {note}"

    def recall(self):
        return self.memory.get_all()

    def forget_all(self):
        self.memory.clear()
        return "Memory cleared"

    # ---- Planner ----
    def add_task(self, task: str):
        self.planner.add_task(task)
        return f"Task added: {task}"

    def next_task(self):
        return self.planner.next_task()

    def peek_tasks(self):
        return self.planner.peek_tasks()

    # ---- DevOps ----
    def check_system(self):
        return self.run_command("uptime")

    # ---- Quick Python ----
    def quick_python(self, code: str):
        return self.run_python(code)
    

