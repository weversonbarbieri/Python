N = int(input("How many numbers do you want to type? "))

vector: [float] = [0 for x in range(N)]

for i in range(0, N):
    vector[i] = int(input("Enter 1 number: "))

print("NEGATIVE NUMBERS: ")
for i in range(0, N):
    if vector[i] < 0:
        print(f"{vector[i]}")