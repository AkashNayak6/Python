import random

number = random.randint(1, 99)

guesses = 0

while guesses < 100:
    guess = int(input("Enter an integer from 1 to 99: "))
    guesses += 1
    print("this is your guess")

    if guess < number:
        print("your guess is low")
    elif guess > number:
        print("your guess is high")
    elif guess == number:
        print("your guess is correct, congratulations!")
        break
