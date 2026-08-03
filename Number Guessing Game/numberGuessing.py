import random

num = random.randrange(1,100)

print("Welcome to the Number Guessing Game!")
print("You are to guess a  number between 1 and 100, and I'll tell you if you're toohigh or low. You have 10 chances to guess it correctly.")

count = 0

while count <= 10:
    if count == 10:
        print("This is your last chance, make it count!")
    guess = int(input(f"Guess no {count + 1} : "))
    if guess == num:
        print(f"Congratulations! You have guessed the number {num} correctly in the {count + 1}th attempt.")
        break
    closeness = (num - guess)
    if abs(closeness) <= 10:
        print("You're very close!")
        if closeness > 0:
            print("Guess higher.")
        elif closeness < 0:
            print("Guess lower.")
    elif abs(closeness) <= 25:
        print("You're close.")
    else:
        print("You're far away.")
    count += 1