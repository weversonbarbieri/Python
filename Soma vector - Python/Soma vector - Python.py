sumvector: float; average: float

N = int(input("How many numbers do want to type? "))

vector: [float] = [0 for x in range(N)]

for i in range(0, N):
    vector[i] = float(input("Enter 1 number: "))

print()
print("VALUE = ", end="")
for i in range(0, N):
    print(f"{vector[i]} ", end="")

print()
sumvector = 0
for i in range(0, N):
    sumvector = sumvector + vector[i]
    average = sumvector / N

print(f"SUM VECTOR = {sumvector:.2f}")
print((f"AVERAGE = {average:.2f}"))
