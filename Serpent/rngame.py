from random import *

print('''Welcome to a simple guess the number game! You will be able to select a range and from there a number shall be chosen.
If you want the extra challenge you may enable lives and state how many chances you wish to have :)''')
Error1 = 'Error: This variable requires an integer value, please try again.'
Error2 = 'Error: This variable requires a (Y)ES or (N)O answer, please try again.'

running = True
Attempt = 0
Answer = 0
valid = ('yes', 'y', 'no', 'n')

def generate():
    global Answer
    High = True
    Low = True

    while High == True:
        try:
            High = int(input("What is the upper limit? "))
        except ValueError:
        #    print(type(High))   # <<DEBUG>>
            print(Error1)
            High = int(input("What is the upper limit? "))
            if type(High) == int or High == 0:
                continue
        else:
            continue

    while Low == True:
        try:
            Low = int(input("What is the lower limit? "))
        except ValueError:
            print(Error1)
            Low = int(input("What is the lower limit? "))
            print(type(Low))
            if type(Low) == int or Low.is_integer == True:
                continue
        else:
            continue
    Answer = randint(Low, High)
    return Answer

def lives():
    Chances = False
    while Chances == False:
        try:
            Chances = int(input("How many lives would you like? "))
        except ValueError:
            print(Error1)
            Chances = int(input("How many lives would you like? "))
            if type(Chances) == int:
                continue
        else:
            print(Chances)
            continue

def guess():
    global Attempt, guess_mode, Chances
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

while running:
    generate()
    choice = False
    while choice == False:
        try:
            choice = str(input("Would you like to enable lives? "))
        except ValueError:
            print(Error2)
            choice = str(input("Would you like to enable lives? "))
            if choice.lower() in valid:
                continue

    if choice.lower() == "y" or choice.lower() == "yes":
        print('Lives enabled')
        lives()     # Lives now enable but need to filter a way that they only follow 
        limit = True
    elif choice.lower() == 'n' or choice.lower() == 'no':
        limit = False
        guess_mode = True
        print('Guess: ')
        while guess_mode:
            guess()
    
    Another = input("Would you like to play again? ")
    if Another.lower() == "no" or Another.lower() == "n":
        break