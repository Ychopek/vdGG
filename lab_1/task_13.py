import random
numb = random.randint(1,100)
while True:
    guess = int(input("Введите число: "))
    print(guess)
    if guess < numb:
        print("numb больше")
    elif guess > numb:
        print("numb меньше")
    else:
        print("угадал!")
        break

