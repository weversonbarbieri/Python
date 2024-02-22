a: int; b: int

print("Enter 2 integer numbers: ")
a = int(input())
b = int(input())

if a % b == 0 or b % a == 0:
    print("THE NUMBERS ARE MULTIPLES")
else:
    print("THE NUMBERS ARE NOT MULTIPLES")