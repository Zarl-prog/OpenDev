import subprocess


def run_command(command):
    try:
        result = subprocess.run(
            command,
            shell=True,
            capture_output=True,
            text=True
        )

        if result.stdout:
            return result.stdout

        if result.stderr:
            return result.stderr

        return "Command executed."

    except Exception as error:
        return f"Command error: {error}"
def read_file(file_path):
    try:
        with open(file_path, "r", encoding="utf-8") as file:
            content = file.read()

        return content

    except Exception as error:
        return f"Error reading file: {error}"