average: float
a: float
b: float
c: float

N = int(input("How many cases do want to enter? "))

for i in range(0, N):
    print("Enter 3 numbers:")
    a = float(input())
    b = float(input())
    c = float(input())
    average = ((a * 2) + (b * 3) + (c * 5)) / 10
    print(f"AVERAGE = {average:.1f}")
