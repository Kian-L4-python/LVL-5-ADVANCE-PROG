import random

def displayMenu():
    print("\nDIFFICULTY LEVEL")
    print("1. Easy")
    print("2. Moderate")
    print("3. Advanced")

def randomInt(difficulty):
    if difficulty == 1:
        return random.randint(1, 9)
    elif difficulty == 2:
        return random.randint(10, 99)
    elif difficulty == 3:
        return random.randint(1000, 9999)

def decideOperation():
    return "+" if random.choice([True, False]) else "-"

def displayProblem(num1, num2, operation):
    while True:
        try:
            return int(input(f"{num1} {operation} {num2} = "))
        except ValueError:
            print("Invalid input. Please enter an integer.")

def isCorrect(user_answer, correct_answer):
    return user_answer == correct_answer

def displayResults(score):
    print("\nQUIZ RESULTS")
    print(f"Your final score is: {score} / 100")
    if score > 90:
        print("Rank: A+")
    elif score > 80:
        print("Rank: A")
    elif score > 70:
        print("Rank: B")
    elif score > 60:
        print("Rank: C")
    else:
        print("Rank: Try Again!")

def quiz():
    displayMenu()
    while True:
        try:
            difficulty = int(input("Select a difficulty level (1, 2, or 3): "))
            if difficulty in [1, 2, 3]:
                break
            else:
                print("Please choose a valid difficulty level.")
        except ValueError:
            print("Invalid input. Please enter 1, 2, or 3.")

    score = 0
    for _ in range(10):
        num1 = randomInt(difficulty)
        num2 = randomInt(difficulty)
        operation = decideOperation()
        correct_answer = num1 + num2 if operation == "+" else num1 - num2

        print("\nNew Problem:")
        user_answer = displayProblem(num1, num2, operation)

        if isCorrect(user_answer, correct_answer):
            print("Correct! You earn 10 points.")
            score += 10
        else:
            print("Incorrect. Try again!")
            user_answer = displayProblem(num1, num2, operation)
            if isCorrect(user_answer, correct_answer):
                print("Correct! You earn 5 points.")
                score += 5
            else:
                print(f"Incorrect again! The correct answer was {correct_answer}.")

    displayResults(score)

def main():
    while True:
        quiz()
        play_again = input("\nWould you like to play again? (yes/no): ").strip().lower()
        if play_again != 'yes':
            print("Thank you for playing! Goodbye!")
            break

if __name__ == "__main__":
    main()
