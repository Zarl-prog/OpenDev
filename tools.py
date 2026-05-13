import subprocess


def run_command(command):
    try:
        result = subprocess.run(command, shell=True, capture_output=True, text=True)

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


def write_file(file_path, content):
    try:
        with open(file_path, "w", encoding="utf-8") as file:
            file.write(content)

        return f"Successfully wrote to {file_path}"

    except Exception as error:
        return f"Write error: {error}"
