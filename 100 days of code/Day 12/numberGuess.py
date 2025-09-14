import random
import sys

print("Welcome to the number guessing game!")
difficulty = input("Enter the difficulty \"easy\" or \"hard\": ")

if difficulty == "easy":
    attempts = 10
elif difficulty == "hard":
    attempts = 5
else:
    print("wrong input")
    sys.exit(0)
number = random.randint(1, 101)
print(f"You have {attempts} attempts to guess the number betwean 1 - 100")

while attempts != 0:
    guess = int(input("Enter the number: "))
    if guess == number:
        print("You win")
        break
    if guess < number:
        print("Too low")
        attempts -= 1
        print(f"{attempts} attempts remaining")
    elif guess > number:
        print("Too high")
        attempts -= 1
        print(f"{attempts} attempts remaining")