print ("enter your birth date (day)")
day = int(input())
print("enter your date (month)")
month = int(input())
zodiac = [
    ("Козерог", (12, 22)),
    ("Водолей", (1, 20)),
    ("Рыбы", (2, 19)),
    ("Овен", (3, 21)),
    ("Телец", (4, 20)),
    ("Близнецы", (5, 21)),
    ("Рак", (6, 21)),
    ("Лев", (7, 23)),
    ("Дева", (8, 23)),
    ("Весы", (9, 23)),
    ("Скорпион", (10, 23)),
    ("Стрелец", (11, 22)),
    ("Козерог", (12, 22))
]
for i in range(len(zodiac) - 1):
    name, (nextmonth, nextday) = zodiac[i + 1]
    prevmonth, prevday = zodiac[i][1]
    if (month == prevmonth and day >= prevday) or (month == nextmonth and day <= nextday):
        print("your zodiac sign:", zodiac[i][0])
        break
