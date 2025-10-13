print ("Enter X rubles")
sum = int(input())
print (sum // 100, "x100")
sum %= 100
print (sum // 50, "x50")
sum %= 50
print (sum // 10, "x10")
sum %= 10
print (sum // 5, "x5")
sum %= 5
print (sum // 2, "x2")
sum %= 2
print (sum // 1, "x1")