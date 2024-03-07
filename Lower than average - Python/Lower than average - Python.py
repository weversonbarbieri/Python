average: float
sum: float

N = int(input("How many elements will have the vector? "))
vector = [0 for x in range(N)]

for i in range(0, N):
    vector[i] = float(input("Enter 1 number: "))

print()
sum = 0
for i in range(0, N):
    sum = sum + vector[i]

average = sum / N
print(f"AVERAGE VECTOR = {average:.3f}")
print("ELEMENTS LOWER THAN AVERAGE:")
for i in range(0, N):
    if vector[i] < average:
        print(f"{vector[i]}")