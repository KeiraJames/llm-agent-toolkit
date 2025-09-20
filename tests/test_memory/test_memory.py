from modules.memory.memory import Memory

def test_memory_add_and_get():
    mem = Memory()
    mem.add("task1")
    mem.add("task2")
    all_items = mem.get_all()
    assert all_items == ["task1", "task2"]

def test_memory_clear():
    mem = Memory()
    mem.add("task")
    mem.clear()
    assert mem.get_all() == []
