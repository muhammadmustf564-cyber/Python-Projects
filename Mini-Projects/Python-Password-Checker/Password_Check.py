import string
x = input("Enter password:")
special_chars = "#$@!%^/?"
if  len(x) <= 9 and any(char in special_chars for char in x) and any(char.isupper() for char in x)and any(char.islower() for char in x) and any(char.isdigit() for char in x):
     print(x,"=> strong password")
else:
    print(x,"=> weak password")
