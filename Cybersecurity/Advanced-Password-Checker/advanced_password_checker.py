found = False
count = 0

for attempt in range(3):
  password = input("Enter password:")

  errors = []

  if len(password) < 8:
    errors.append("Password must at least 8 character")

  if not any(c.isupper() for c in password):
    errors.append("missing uppercare letter")

  if not any(c.islower() for c in password):
    errors.append("missing lowercase character")

  if not any(c.isdigit() for c in password):
    errors.append("missing digit")

  if not any(not c.isalnum() for c in password):
    errors.append("missing special letter")

  if len(errors) == 0:
    print("Strong password")

    found = True
    break
  
  elif len(errors) <=  2:
    print("Medium Password")
    print("Reason:")

    for e in errors:
      print("-", e)

    count += 1
    print(f"attemp {count} is medium")

  else:
    print("Weak Password")
    print("Reason:")

    for e in errors:
        print("-", e)

    count +=1
    print(f"attempt {count} is weak")

else:
  print("Account Locked")