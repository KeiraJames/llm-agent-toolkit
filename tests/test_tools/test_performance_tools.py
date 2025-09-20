import time
from modules.tools.performance_tools import time_execution

def test_time_execution_runs_function():
    def sample():
        time.sleep(0.1)
        return 42
    result, elapsed = time_execution(sample)
    assert result == 42
    assert elapsed >= 0.1
