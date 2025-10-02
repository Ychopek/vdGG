print ("Enter the string")
str = input()
flag = True
for i in range(0,len(str)):
    if str[i] != str[-i-1]:
        print("not palindrome")
        flag = False
        break
    else:
        continue
if flag:
    print(str, "is palindrome")
