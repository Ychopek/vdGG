#Дан список строк. Найдите строку с наибольшим количеством символов "a".
stroki = input().split()
print(list(sorted(stroki,key = lambda x: x.count("a"),reverse=True))[0])
