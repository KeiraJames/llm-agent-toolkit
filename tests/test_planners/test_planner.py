from modules.planners.planner import Planner

def test_add_and_next_task():
    planner = Planner()
    planner.add_task("task1")
    planner.add_task("task2")
    assert planner.next_task() == "task1"
    assert planner.next_task() == "task2"
    assert planner.next_task() is None

def test_peek_tasks():
    planner = Planner()
    planner.add_task("task1")
    planner.add_task("task2")
    assert planner.peek_tasks() == ["task1", "task2"]
