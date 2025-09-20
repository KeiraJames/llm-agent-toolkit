from agents.base_agent import BaseAgent

def test_base_agent_act():
    agent = BaseAgent("TestAgent")
    agent.act("Say hi")