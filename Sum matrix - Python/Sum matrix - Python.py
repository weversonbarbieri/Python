
M = int(input("Enter the quantity lines: "))
N = int(input("Enter the quantity column: "))


matrix1 = [[0 for x in range(N)] for x in range(M)]
matrix2 = [[0 for x in range(N)] for x in range(M)]
matrixAB = [[0 for x in range(N)] for x in range(M)]

print("Enter the value of matrix A:")
for i in range(0, M):
    for j in range(0, N):
        matrix1[i][j] = int(input(f"Elemento [{i},{j}]: "))

print("Enter the value of matrix B:")
for i in range(0, M):
    for j in range(0, N):
        matrix2[i][j] = int(input(f"Elemento [{i},{j}]: "))

for i in range(0, M):
    for j in range(0, N):
        matrixAB[i][j] = matrix1[i][j] + matrix2[i][j]

print("MATRIX SOMA:")
for i in range(0, M):
    for j in range(0, N):
        print(f"{matrixAB[i][j]} ", end="")
    print()

