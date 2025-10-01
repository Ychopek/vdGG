print("enter the number:")
numb = int(input())
sum = 0
if numb % 7 == 0:
    print("Magic number!")
elif numb == 0:
    print("Zero!!!")
else:
    while numb > 0:
        sum += numb % 10
        numb //= 10
    print (sum)