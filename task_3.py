print("Enter a password:")
password = input()
if len(password) < 16:
    print("too short")
elif password.isalpha() == True or password.isdigit() == True:
    print("weak password")
else:
    print("good password")
