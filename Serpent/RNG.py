import random, time
loop = True
Generate = True
low = 0
high = 0
print(" ")

def wait(sec):
    while sec > 0:
        time.sleep(1)
        print(".")
        sec = sec - 1
        # print(wait)   [DEBUG]

def main():
    while True:
        low = int(input("Please choose the lowest number: "))
        high = int(input("Please choose the highest number: "))
    
        print("Generating a random number between " + str(low) + " and " + str(high))
        
        while True:
            wait(3)
            result = random.randint(int(low),int(high))
            time.sleep(1)
            print(result)

            Repeat = input("Would you like to repeat? [Y/N] ").lower()
            if Repeat != "y":
                break 

        choice = input("Would you like to generate more values? [Y/N] ").lower()
        if choice != "y":
            print("closing program...")
            print(" ")
            time.sleep(1)
            break

main()
