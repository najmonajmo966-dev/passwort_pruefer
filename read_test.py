with open("comon.txt") as file:
    passwords = file.read()

passwords = passwords.splitlines()

password = input("Enter your password: ")
if password in passwords:
    print("red flag")
else:
    print("green flag")