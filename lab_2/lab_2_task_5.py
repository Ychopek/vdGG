#Дан список чисел. Найдите сумму всех положительных чисел.
lst = [int(input()),int(input()),int(input()),int(input())]
print(sum(i for i in lst if i > 0))