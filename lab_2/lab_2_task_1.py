#Напишите программу, которая выводит все простые числа от 1 до N
N = input("enter the N:")
print(*list(filter(lambda x: x > 1 and all(x % i != 0 for i in range(2, int(x / 2) + 1)), range(1, int(N) + 1))))