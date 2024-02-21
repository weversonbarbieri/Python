import math

delta: float; x1: float; x2: float; a: float; b: float; c: float

a = float(input("Enter A value: "))
b = float(input("Enter B value: "))
c = float(input("Enter C value: "))

delta = pow(b, 2) - (4 * a * c)

if delta < 0:
    print("This equation does not have a solution!")
else:
    x1 = (- b + math.sqrt(delta)) / (2 * a)
    x2 = (- b - math.sqrt(delta)) / (2 * a)

    print(f"X1 = {x1:.4f}")
    print(f"X2 = {x2:.4f}")



