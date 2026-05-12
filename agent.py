from llm import ask_llm

def run_agent():
    while True:
        user_input = input("\nYou: ")

        if user_input.lower() == "exit":
            break

        response = ask_llm(user_input)

        print("\nOpenDev:")
        print(response)