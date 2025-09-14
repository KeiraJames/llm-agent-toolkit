import subprocess

def run_command(command: str) -> str:    
    try:
        result = subprocess.run(command, shell=True, check=True, capture_output=True, text=True)
        return result.stdout.strip()
    
    except subprocess.CalledProcessError as e:
        return "Error: ", {e}
