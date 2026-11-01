import matplotlib.pyplot as plr

active = True
def collatz():
    startValue = int(input("Please enter a value greater than one: "))
    useValue = startValue
    n = 0
    while active:
        test = useValue % 2
        if test > 0 and useValue != 1:
            useValue = (useValue * 3) + 1
            n = n + 1
            print(str(n) + ": " + str(useValue))
        elif test == 0 and useValue != 1:
            useValue = useValue / 2
            n = n + 1
            print(str(n) + ": " + str(useValue))
        elif useValue == 1:
            print("You started with " + str(startValue))
            print("After " + str(n) + " runs you reached 1")
            break
