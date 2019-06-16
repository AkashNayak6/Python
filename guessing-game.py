import random

number = random.randint(1, 99)

guesses = 0

while guesses < 100:
    guess = int(input("Enter an integer from 1 to 99: "))
    guesses += 1
    print("this is your %d guess")

    if guess < number:
        print("guess is low")
    elif guess > number:
        print("guess is high")
    elif guess == number:
        print("guess correct!")
        break
