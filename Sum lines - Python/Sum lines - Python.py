
M = int(input("Enter the line quantity: "))
N = int(input("Enter the column quantity: "))

matrix = [[0 for x in range(N)] for x in range(M)]
vector = [0 for x in range(N)]

for i in range(0, M):
    print(f"Enter the elements of the {i + 1}a line: ")
    for j in range(0, N):
        matrix[i][j] = float(input())

print("VECTOR GENERATED:")
vector[i] = 0
for i in range(0, M):
    for j in range(0, N):
        vector[i] = vector[i] + matrix[i][j]

    print(f"{vector[i]}")