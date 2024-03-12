
M = int(input("Enter the line quantity: "))
N = int(input("Enter the column quantity: "))

matrix = [[0 for x in range(N)] for x in range(M)]

for i in range(0, M):
    for j in range(0, N):
        matrix[i][j] = int(input(f"Elemento [{i},{j}]: "))

print("NEGATIVE VALUES:")
for i in range(0, M):
    for j in range(0, N):
        if matrix[i][j] < 0:
            print(f"{matrix[i][j]}")