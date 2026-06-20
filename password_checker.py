password = input("Enter Password: ")

score = 0

if len(password) >= 8:
    score += 1

has_upper = False
for ch in password:
    if ch.isupper():
        has_upper = True

if has_upper:
    score += 1

has_number = False
for ch in password:
    if ch.isdigit():
        has_number = True

if has_number:
    score += 1

if score == 1:
    print("Weak Password")
elif score == 2:
    print("Medium Password")
else:
    print("Strong Password")
