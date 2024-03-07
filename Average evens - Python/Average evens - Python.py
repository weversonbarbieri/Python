sum: int
quantityevens:  int
average: float

N = int(input(" How many elements will contain the vector? "))

vector = [0 for x in range(N)]

for i in range(0, N):
    vector[i] = int(input("Enter 1 numero: "))

sum = 0
quantityevens = 0
for i in range(0, N):
    if vector[i] % 2 == 0:
        quantityevens = quantityevens + 1
        sum = sum + vector[i]

if quantityevens == 0:
    print("NO EVEN NUMBER ENTERED")
else:
    average = sum / quantityevens
    print(f"EVERAGE EVENS = {average:.1f}")
