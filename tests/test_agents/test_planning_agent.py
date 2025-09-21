from agents.planning_agent import PlanningAgent

def test_planning_agent_memory_and_tasks():
    agent = PlanningAgent("TestBot")
    agent.remember("my favorite color is red")
    assert "my favorite color is red" in agent.recall_all()

    agent.add_task("task1")
    assert agent.peek_tasks() == ["task1"]
    assert agent.next_task() == "task1"
