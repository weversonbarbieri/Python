a: int; b: int; c: int

a = int(input("Enter the 1st value: "))
b = int(input("Enter the 2nd value: "))
c = int(input("Enter the 3rd value: "))

if a < b and a < c:
    print(f"LOWER NUMBER = {a}")
elif b < a and b < c:
    print(f"LOWER NUMBER = {b}")
else:
    print(f"LOWER NUMBER = {c}")