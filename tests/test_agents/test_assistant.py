from agents.assistant import Assistant

def test_memory_and_tasks(monkeypatch):
    bot = Assistant()

    # ---- Memory ----
    bot.remember("Learn pytest")
    assert "Learn pytest" in bot.recall()

    bot.remember("Write unit tests")
    assert bot.recall() == ["Learn pytest", "Write unit tests"]

    bot.forget_all()
    assert bot.recall() == []

    # ---- Planner ----
    bot.add_task("task1")
    bot.add_task("task2")
    assert bot.next_task() == "task1"
    assert bot.peek_tasks() == ["task2"]

    # ---- DevOps and Python mocks ----
    monkeypatch.setattr(bot, "run_command", lambda cmd: "mock-uptime")
    monkeypatch.setattr(bot, "run_python", lambda code: "42")

    assert bot.check_system() == "mock-uptime"
    assert bot.quick_python("print(1)") == "42"
