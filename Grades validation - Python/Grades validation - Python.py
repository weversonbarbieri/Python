a: float; b: float; averagegrades: float

a = float(input("Enter the 1st grade: "))
while a < 0 or a > 10:
    a = float(input("Invalid grade! Try again: "))


b = float(input("Enter the 2nd grade: "))
while b < 0 or b > 10:
    b = float(input("Invalid grade! Try again: "))


averagegrades = (a + b) / 2

print(f"AVERAGE = {averagegrades:.2f}")