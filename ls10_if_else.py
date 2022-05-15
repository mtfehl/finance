"""Example of if-then-else statement(s)."""

THE_ANSWER_TO_LIFE_THE_UNIVERSE_AND_EVERYTHING: int = 42
YES: str = "Yes"

print("Guess a number...")

guess: int = int(input("Your Guess: "))

if guess == THE_ANSWER_TO_LIFE_THE_UNIVERSE_AND_EVERYTHING:
    print("Correct!")
    print("Congratulations! You're a winner!")
else:
    print("Incorrect! Try again?")
    try_again: str = input("")
    if try_again == YES:
        print("Guess a number...")
        guess: int = int(input("Your Guess: "))
    else:
        print("Game over")
   








