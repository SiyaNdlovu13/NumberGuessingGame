import random

number = random.randint(1, 100)
print("Computer selected a number from 1 to 100 (inclusive), now your turn -")

turns = 0

while True:
    guess = int(input("Guess a number = "))
    if guess == number:
        print("You got it right")
        break

    elif guess < number:
        print("Guess a bigger number")
        turns += 1

    elif guess > number:
        print("Enter smaller number please ")
        turns += 1

print("Number of turns = ", turns + 1)