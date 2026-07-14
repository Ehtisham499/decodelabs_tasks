print("=" * 40)
print("🤖 Welcome to RuleBot!")
print("Type 'help' to see available commands.")
print("Type 'exit' to quit.")
print("=" * 40)

while True:
    user = input("\nYou: ").strip().lower()

    if user in ["hi", "hello", "hey"]:
        print("Bot: Hello! Nice to meet you.")

    elif user == "how are you":
        print("Bot: I'm doing great! Thanks for asking.")

    elif user == "what is your name":
        print("Bot: My name is RuleBot.")

    elif user == "who made you":
        print("Bot: I was created by Ehtisham Sabir as a Python project.")

    elif user == "help":
        print("Available commands:")
        print("- hi")
        print("- hello")
        print("- how are you")
        print("- what is your name")
        print("- who made you")
        print("- bye")
        print("- exit")

    elif user == "bye":
        print("Bot: Goodbye! Have a great day!")

    elif user == "exit":
        print("Bot: Thank you for using RuleBot. Goodbye!")
        break

    else:
        print("Bot: Sorry, I don't understand that command.")
        break