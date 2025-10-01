'''
Collatz conjecture, Start with a number n > 1.
If n is even, divide it by 2. 
If n is odd, multiply it by 3 and add 1.
'''
print(" ") # adds some apace
def main():
    start_value = int(input("Please enter a value > 1: "))
    use_value = start_value
    n = 0

    while True:
        test = use_value % 2
        # print("test: " + str(test))   [DEBUG]
        if test > 0 and use_value != 1:
            use_value = (use_value * 3) + 1
            n = n + 1
            print(str(n) + ": " + str(use_value))
        elif test == 0 and use_value != 1:
            use_value = use_value / 2
            n = n + 1
            print(str(n) + ": " + str(use_value))
        elif use_value == 1:
            print("You started with " + str(start_value))
            print("After " + str(n) + " runs you reached 1")
            break
print(" ") # adds some space on the end.
main()
