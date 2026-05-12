from llm import ask_llm
from tools import read_file, run_command


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

        else:
            response = ask_llm(user_input)

        print("\nOpenDev:")
        print(response)