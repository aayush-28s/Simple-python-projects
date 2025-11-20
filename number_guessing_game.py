import random

random = random.randint(1, 100)
guess = 0

while True:
    try:
        guess = int(input("Guess the number between 1 and 100: "))

        if guess < random:
            print("Sorry! You guessed too low.")

        elif guess > random:
            print("Sorry! You guessed too high.")

        else:
            print("Congratulations! You guessed right!")
            break

    except ValueError:
        print("Sorry, you didn't enter a number.")