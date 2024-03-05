higher: float
higherposition: int

N = int(input("How many numbers do want to type? "))

vector = [0 for x in range(N)]

for i in range(0, N):
    vector[i] = float(input("Enter 1 number: "))

higher = i
for i in range(0, N):
    if vector[i] > higher:
        higher = vector[i]
        higherposition = i

print()
print(f"HIGHER VALUE = {higher:.1f}")
print(f"HIGHER POSITION = {higherposition}")