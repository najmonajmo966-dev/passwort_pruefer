password = input("Enter your password: ")

length = len(password)
print(f"length:{length}")
if length < 8:
    print("The password too short")
elif length > 16:
    print("The password too long")
else :
    print("The length is ok")

found_digit = False
found_upper = False
found_lower = False
found_another_symbol = False

for letter in password :
    if letter.isdigit():
        found_digit = True
    elif letter.isupper():
        found_upper = True
    elif letter.islower():
        found_lower = True
    else :
        found_another_symbol = True


print(f"Digit:{found_digit}")
print(f"Upper:{found_upper}")
print(f"Lower:{found_lower}")
print(f"Symbol:{found_another_symbol}")

points = 0
if found_digit :
    points += 1
if found_upper :
    points += 1
if found_lower :
    points += 1
if found_another_symbol :
    points += 1
print(f"score:{points}")

with open("comon.txt") as file:
    passwords = file.read().lower()

passwords = passwords.splitlines()

if password.lower() in passwords:
    print("dangerous password")
elif length >= 8 and points == 4:
    print("Strong")
elif length >= 8 and points >= 2:
    print("Medium")
else:
    print("Weak")




