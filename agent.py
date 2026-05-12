from llm import ask_llm
from tools import read_file


def run_agent():
    while True:
        user_input = input("\nYou: ")

        if user_input.lower() == "exit":
            break

        if user_input.startswith("read "):
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

        else:
            response = ask_llm(user_input)

        print("\nOpenDev:")
        print(response)