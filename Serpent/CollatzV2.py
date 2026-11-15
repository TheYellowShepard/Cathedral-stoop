import matplotlib.pyplot as plt
import numpy as np

answer = 1
runData = {}
running = True

def testValue():
    global startValue
    test = True

    while test:
        try:
            test = int(input("Enter an integer value greater than one: "))
        #    print(test)
        except ValueError:
            print("Error")
            test = int(input("Enter an integer value greater than one: "))
            if type(test) == int:
                print("continue1")
                continue
        else:
            if test > 1:
                startValue = test
                return startValue
            else:
                print("error2")
                continue

def data():
    useValue = startValue
    n=0
    initiate = True
    while initiate:
        check = useValue % 2
        runData.update({n:useValue})
        if check == 0 and useValue != 1:
            useValue = useValue / 2
            n += 1
        elif check != 0 and useValue != 1:
            useValue = (useValue * 3) + 1
            n += 1
        elif useValue == 1:
            print("Complete")            
            print(runData) # DEBUG
            break  # DEBUG

def display():
    x = runData.keys()
    y = runData.values()
    fig, ax = plt.subplots()
    ax.plot(x, y, linewidth=2.0)
    
    plt.show()


while running:
    testValue()
    data()
    display()
    running = False