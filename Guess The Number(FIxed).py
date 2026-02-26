import random

answer = random.randint(1, 100)
user = 0
attempts = 0
print(answer)
print("Guess a number between 1 and 100!")

while user != answer:
    try:
        user = int(input("\nType Your Guess! (Use Only Numbers)"))
        attempts = attempts + 1 # Increment attempts with each valid guess

    except ValueError:
        print("Please enter a valid number.")
        continue

    if user == answer:
        if answer > 67:
            print("\nThe Answer was Bigger than 67!")
        else:
            print("\nThe Answer was Smaller than 67!")

        print(f"\nYou Are Correct! The answer was {answer}\n")
        score = 120 - attempts * 10
        print(f"Your Score Was: {score}")
        break # Exit the loop once the correct answer is guessed

    elif user > answer:
        attempts = attempts + 1
        print("\nPick a Smaller Number! Your guess was too high!\n")
    else:
        attempts = attempts + 1
        print("\nPick a Bigger Number! Your guess was too low!\n")
