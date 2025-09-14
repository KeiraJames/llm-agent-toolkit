from agents.base_agent import BaseAgent
from modules.tools.shell_tools import run_command

class DevOpsAgent(BaseAgent):
    def act(self, task):
        if task == "check system":
            return run_command("uptime")
        return super().act(task)
