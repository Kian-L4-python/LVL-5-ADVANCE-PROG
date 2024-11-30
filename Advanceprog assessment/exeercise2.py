import random

def load_jokes(filename):
    jokes = []
    try:
        with open(filename, 'r') as file:
            for line in file:
                if "?" in line:
                    setup, punchline = line.strip().split("?", 1)
                    jokes.append((setup.strip(), punchline.strip()))
        if not jokes:
            raise ValueError("The jokes file is empty.")
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")
        exit()
    except Exception as e:
        print(f"Error reading jokes: {e}")
        exit()
    return jokes

def tell_joke(jokes):
    setup, punchline = random.choice(jokes)
    print(f"\n{setup}?")
    input("Press Enter to see the punchline...")
    print(f"{punchline}\n")

def main():
    jokes = load_jokes("randomJokes.txt")
    print("Welcome to the Joke Teller!")
    print('Ask me for a joke by typing "Alexa tell me a joke" or type "quit" to exit.')

    while True:
        user_input = input("\nYour command: ").strip().lower()
        if user_input == "alexa tell me a joke":
            tell_joke(jokes)
        elif user_input == "quit":
            print("Goodbye! Hope you had a laugh!")
            break
        else:
            print('Invalid command. Type "Alexa tell me a joke" or "quit".')

if __name__ == "__main__":
    main()
