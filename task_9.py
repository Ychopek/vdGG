print ("enter the IP:")
IP = input()
flag = True
parts = IP.split(".")
if len(parts) != 4:
    flag = False
else:
    for part in parts:
        if not part.isdigit() or not 0 <= int(part) <= 255:
            flag = False
            break
if flag:
    print(IP, "is valid IP")
else:
    print(IP, "is invalid IP")
