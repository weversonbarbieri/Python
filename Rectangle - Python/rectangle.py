import math

base = float(input("Enter the rectangle base: "))
height = float(input("Enter the rectangle height: "))

area = base * height
perimeter = 2 * (base + height)
diagonal = math.sqrt(base ** 2 + height ** 2)


print(f"AREA = {area:.4f}")
print(f"PERIMETER = {perimeter:.4f}")
print(f"DIAGONAL = {diagonal:.4f}")
