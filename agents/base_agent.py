class BaseAgent:
    def __init__(self, name):
        self.name = name

    def act(self, task):
        print(f"{self.name} received a task: {task}" )

