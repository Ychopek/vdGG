#Дан список строк. Найдите длину самой короткой строки.
spisok = [input(), input(), input(), input(), input()]
#nextspisok = sorted(spisok, key = len)[0]
#print(len(nextspisok[0]))
print(len(sorted(spisok, key = len)[0]))