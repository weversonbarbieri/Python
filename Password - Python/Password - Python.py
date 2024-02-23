password: int

password = int(input("Enter the password: "))

while password != 2002:
    password = int(input("Invalid password! Try again: "))

print("Access granted!")