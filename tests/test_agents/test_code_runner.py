from modules.tools.code_runner import run_python

def test_run_python_prints_output():
    code = "print('hello')"
    output = run_python(code).strip()
    assert output == "hello"
