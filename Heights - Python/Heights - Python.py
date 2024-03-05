sumheights: float
averageheights: float
percentage: float
sumages: int

N = int(input("How persons do want to type? "))

vectornames = [0 for x in range(N)]
vectorages = [0 for x in range(N)]
vectorheigths = [0 for x in range(N)]

for i in range(0, N):
    vectornames[i] = str(input("Name: "))
    vectorages[i] = int(input("Age: "))
    vectorheigths[i] = float(input("Heigth: "))


print()
sumheights = 0
for i in range(0, N):
    sumheights = sumheights + vectorheigths[i]

averageheights = sumheights / N
print(f"AVERAGE = {averageheights:.2f}")

sumages = 0
for i in range(0, N):
    if vectorages[i] < 16:
        sumages = sumages + 1

percentage = (sumages * 100) / N
print(f"People lower than 16 years old: {percentage:.1f}%")

for i in range(0, N):
    if vectorages[i] < 16:
        print(f"{vectornames[i]}")

