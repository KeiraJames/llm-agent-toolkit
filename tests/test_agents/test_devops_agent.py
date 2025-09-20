import agents.devops_agent as devops_agent

def test_devops_agent_check_system(monkeypatch):
    monkeypatch.setattr(devops_agent, "run_command", lambda cmd: "mock-uptime")

    agent = devops_agent.DevOpsAgent("Tester")
    result = agent.act("check system")

    assert result == "mock-uptime"
