#Напишите программу, которая вычисляет факториал числа N с помощью цикла for.
N = input("enter the N:")
factor = 1
for i in range(1, int(N) + 1):
    factor *= i
print(factor)
