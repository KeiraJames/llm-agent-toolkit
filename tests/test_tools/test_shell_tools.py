from modules.tools.shell_tools import run_command

def test_run_command():
    output = run_command("echo hello")
    assert output == "hello"
