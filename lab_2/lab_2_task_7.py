#Напишите программу, которая генерирует словарь с ключами-числами от 1 до N, а значениями — их обратные значения.
N = int(input("enter the N:"))
my_dict = {}
for i in range(1, N + 1):
    my_dict[str(i)] = str(round(1 / i,2))

print(my_dict.items())