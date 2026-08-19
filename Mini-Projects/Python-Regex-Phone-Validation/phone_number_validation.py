import re 
n = input("Enter a number: ")
match = re.search(r'^[789]\d{9}$',n)
if match:
    print("Yes")
else:
    print("No")