import random
#
n = random.randint(1, 100)
guess = int(input("Введите число: "))
while n!= guess:
    if guess < n:
        print("Меньше")
        guess = int(input("Напишите число заново: "))
    elif guess > n:
        print("Больше")
        guess = int(input("Напишите число заново: "))
    else:
        break
    print("Правильно")
    break