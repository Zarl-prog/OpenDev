from llm import ask_llm
from tools import read_file, run_command, write_file, web_search


def run_agent():
    while True:
        user_input = input("\nYou: ")

        if user_input.lower() == "exit":
            break

        elif user_input.startswith("read "):
            file_path = user_input.replace("read ", "")

            print("Reading file...")

            file_content = read_file(file_path)[:3000]

            print("File loaded.")

            prompt = f"""
Analyze this file:

{file_content}
"""

            print("Sending to LLM...")

            response = ask_llm(prompt)

            print("LLM responded.")

        elif user_input.startswith("run "):
            command = user_input.replace("run ", "")

            print("Executing command...")

            output = run_command(command)

            response = f"""
Command Output:

{output}
"""
        elif user_input.startswith("search "):
            query = user_input.replace("search ", "")
            print("Searching the web...")
            response = web_search(query)
        elif user_input.startswith("write "):
            parts = user_input.split(" ", 2)

            if len(parts) < 3:
                response = "Usage: write filename content"

            else:
                file_path = parts[1]
                content = parts[2]

                print("Writing file...")

                response = write_file(file_path, content)
        else:
            response = ask_llm(user_input)

        print("\nOpenDev:")
        print(response)
