a: float
b: float
c: float

print("Enter 3 numbers: ")
a = float(input())
b = float(input())
c = float(input())

if a > b and a > c:
    print(f"HIGHER NUMBER = {a:.2f}")
elif b > a and b > c:
    print(f"HIGHER NUMBER = {b:.2f}")
else:
    print(f"HIGHER NUMBER = {c:.2f}")