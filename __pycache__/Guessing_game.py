import random

winning_number = random.randint(0, 100)
guess = None
num_attempts = 0

while guess != winning_number:
    try:
        guess = int(input("Enter a number between 1 and 100: "))
        num_attempts += 1
        if guess < winning_number:
            print("Guess higher.")
        elif guess > winning_number:
            print("Guess lower.")
    except ValueError:
        print("That's not a valid number. Try again.")

print("Congratulations! You won in {} attempts.".format(num_attempts))