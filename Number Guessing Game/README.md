# 🎯 Number Guessing Game

A simple command-line **Number Guessing Game** built with Python. The computer randomly selects a number between **1 and 100**, and the player has **10 chances** to guess it correctly.

Along the way, the game provides hints indicating whether the guess is **very close**, **close**, or **far away**, making the game more interactive.

---

# 📚 Table of Contents

- [Overview](#overview)
- [Features](#features)
- [Concepts Used](#concepts-used)
- [How the Game Works](#how-the-game-works)
- [Project Structure](#project-structure)
- [Code](#code)
- [Sample Output](#sample-output)
- [Possible Improvements](#possible-improvements)
- [Learning Outcomes](#learning-outcomes)

---

# Overview

This project is a beginner-friendly Python game that demonstrates the use of:

- Random number generation
- Loops
- Conditional statements
- User input
- Mathematical operations
- Basic game logic

The objective is to correctly guess a randomly generated number within the allowed number of attempts.

---

# Features

- 🎲 Random number generation between **1 and 100**
- 🎯 Maximum of **10 attempts**
- 💡 Intelligent hints based on how close the guess is
- 📈 Tells the player whether to guess **higher** or **lower** when very close
- 🎉 Congratulates the player upon winning

---

# Concepts Used

## 1. Modules

The program imports Python's built-in `random` module.

```python
import random
```

The `random` module allows us to generate random values.

---

## 2. Random Number Generation

```python
num = random.randrange(1, 100)
```

`random.randrange(start, stop)` generates a random integer between:

- **Start (inclusive)**
- **Stop (exclusive)**

Therefore,

```python
random.randrange(1,100)
```

generates numbers from **1 to 99**.

> **Note:** If you want the range to include **100**, use:

```python
random.randint(1,100)
```

or

```python
random.randrange(1,101)
```

---

## 3. Variables

Variables store information during program execution.

Example:

```python
num = random.randrange(1,100)
count = 0
guess = int(input())
```

---

## 4. User Input

```python
guess = int(input())
```

- `input()` accepts user input as a string.
- `int()` converts it into an integer.

---

## 5. While Loop

The game continues until:

- The player guesses correctly, or
- The maximum attempts are reached.

```python
while count <= 10:
```

---

## 6. Conditional Statements

The game uses `if`, `elif`, and `else` statements to decide which hint to display.

Example:

```python
if guess == num:
    ...
elif abs(closeness) <= 10:
    ...
else:
    ...
```

---

## 7. Absolute Value

```python
abs(closeness)
```

The `abs()` function returns the absolute value of a number.

Example:

```
abs(-15) = 15
abs(8) = 8
```

This allows the program to measure the distance between the guess and the actual number regardless of whether the guess is too high or too low.

---

# How the Game Works

1. The computer randomly selects a number.
2. The player enters a guess.
3. The game compares the guess with the secret number.
4. Based on the difference, hints are displayed:

| Difference | Hint |
|------------|------|
| 0 | Correct Guess 🎉 |
| ≤ 10 | You're very close! |
| ≤ 25 | You're close. |
| > 25 | You're far away. |

If the guess is within **10**, the game also tells the player to guess **higher** or **lower**.

---

# Project Structure

```
Number-Guessing-Game/
│
├── number_guessing_game.py
└── README.md
```

---

# Code

```python
import random

num = random.randrange(1,100)

print("Welcome to the Number Guessing Game!")
print("You are to guess a number between 1 and 100, and I'll tell you if you're too high or low. You have 10 chances to guess it correctly.")

count = 0

while count <= 10:
    if count == 10:
        print("This is your last chance, make it count!")

    guess = int(input(f"Guess no {count + 1}: "))

    if guess == num:
        print(f"Congratulations! You have guessed the number {num} correctly in the {count + 1}th attempt.")
        break

    closeness = num - guess

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
```

---

# Sample Output

```
Welcome to the Number Guessing Game!

You are to guess a number between 1 and 100.

Guess no 1 : 30

You're far away.

Guess no 2 : 60

You're close.

Guess no 3 : 74

You're very close!

Guess higher.

Guess no 4 : 79

Congratulations!
You have guessed the number 79 correctly in the 4th attempt.
```

---

# Possible Improvements

Some ideas to make the game even better:

- ✅ Validate user input (prevent crashes for non-numeric input)
- ✅ Display remaining attempts
- ✅ Reveal the correct number if the player loses
- ✅ Allow the player to play multiple rounds
- ✅ Add difficulty levels (Easy, Medium, Hard)
- ✅ Track the player's best score
- ✅ Use functions to improve code organization
- ✅ Add colored terminal output using the `colorama` library

---

# Learning Outcomes

By completing this project, you will gain hands-on experience with:

- Python modules
- Random number generation
- Variables
- User input
- Loops
- Conditional statements
- Mathematical operations
- The `abs()` function
- Basic game development logic
- Building interactive command-line applications

---

## 🚀 Future Enhancements

- Difficulty modes
- Scoreboard
- High-score tracking
- Multiple game rounds
- Graphical user interface (GUI) using Tkinter or Pygame
- Sound effects and animations
- Multiplayer mode
- Timer-based challenge mode

---

## 📜 License

This project is intended for learning and educational purposes. Feel free to modify and improve it as you continue your Python journey.
