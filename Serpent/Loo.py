def useless():
    a = 1
    while a != 0:
        a += 1
        print(a)   # [DEBUG]

def iteration():
    numbers = []
    for i, number in numbers:
        number += 1

running = True
while running:
    print('This is a useless loop that does nothing. Press Ctrl+C to stop it.')
    useless()