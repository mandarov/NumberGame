import random

n = random.randint(1, 100)
guess = int(input("Введите число: "))
while n!= guess:
    if guess > n:
        print("")
        guess = int(input(" "))
    elif guess > n:
        print("Больше")
        guess = int(input(" "))
    else:
        break
    print("")
    break