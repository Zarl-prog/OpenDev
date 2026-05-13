import glob
import subprocess

import grep


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


def find_files(pattern):
    try:
        files = glob.glob(pattern, recursive=True)

        if not files:
            return "No matching files found."

        return "\n".join(files)

    except Exception as error:
        return f"Glob error: {error}"

        def search_in_files(search_text):
            try:
                matches = []

                files = glob.glob("**/*", recursive=True)

                for file_path in files:
                    try:
                        with open(file_path, "r", encoding="utf-8") as file:
                            content = file.read()

                            if search_text.lower() in content.lower():
                                matches.append(file_path)

                    except:
                        pass

                if not matches:
                    return "No matches found."

                return "\n".join(matches)

            except Exception as error:
                return f"Grep error: {error}"
