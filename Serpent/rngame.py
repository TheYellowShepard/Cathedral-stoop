from random import *

print('''Welcome to a simple guess the number game! You will be able to select a range and from there a number shall be chosen.
If you want the extra challenge you may enable lives and state how many chances you wish to have :)''')

running = True
Attempt = 0
Answer = 0
Chances = 0

def generate():
    global Answer
    High = int(input("What is the upper limit? "))
    Low = int(input("What is the lower limit? "))
    Answer = randint(Low, High)
    return Answer

def lives():
    global Chances
    Chances = input("How many lives would you like? ")
    return Chances

def guess():
    global Attempt, guess_mode
    Guess = int(input(">>: "))
    if Guess > Answer:
        print("Lower")
        Attempt += 1
        if limit == True and Attempt == Chances:
            print("GAME OVER, the answer was: " + str(Answer))
    elif Guess < Answer:
        print("Higher")
        Attempt += 1
        if limit == True and Attempt == Chances:
            print("GAME OVER, the answer was: " + str(Answer))
    elif Guess == Answer:
        print("Correct")
        guess_mode = False
        print("Attempts: " + str(Attempt))
        if limit == True:
            print("Lives Remaining: " + str(Chances - Attempt))

if running:
    generate()
    choice = input("Would you like to enable lives? ")
    if choice.lower == "y" or choice.lower == "yes":
        lives()
        limit = True
    else:
        limit = False
        guess_mode = True
        while guess_mode:
            guess()
    Another = input("Would you like to play again? ")
    if Another.lower == "no" or Another.lower == "n":
        running = False
    else:
        pass
    