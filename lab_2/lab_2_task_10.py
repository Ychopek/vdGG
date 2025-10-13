#Напишите программу, которая находит сумму всех нечётных чисел от 1 до N.
N = int(input("vvedite N"))
print(sum(filter(lambda x: x % 2 != 0, range(1,N+1))))