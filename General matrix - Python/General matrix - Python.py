sumpositive: float
line: int
column: int
alteratedmatrix: float

N = int(input("Enter the matrix order? "))

matrix = [[0 for x in range(N)] for x in range(N)]

for i in range(0, N):
    for j in range(0, N):
        matrix[i][j] = float(input(f"Elemento [{i},{j}]: "))

print()
print("SUM POSITIVE NUMBER: ", end="")
sumpositive = 0
for i in range(0, N):
    for j in range(0, N):
        if matrix[i][j] > 0:
            sumpositive = sumpositive + matrix[i][j]

print(f"{sumpositive:.1f}")

print()
line = int(input("Choose one line: "))
print("CHOSEN LINE: ", end="")
for j in range(0, N):
    print(f"{matrix[line][j]} ", end="")

print()
print()
column = int(input("Choose one column: "))
print("CHOSEN LINE: ", end="")
for i in range(0, N):
    print(f"{matrix[i][column]} ", end="")

print()
print()
print("MAIN DIAGONAL: ", end="")
for i in range(0, N):
    print(f"{matrix[i][i]} ", end="")

print()
print()
print("ALTERATED MATRIX:")
for i in range(0, N):
    for j in range(0, N):
        if matrix[i][j] < 0:
            alteratedmatrix = pow(matrix[i][j], 2)
            print(f"{alteratedmatrix:.1f} ", end="")
        else:
            print(f"{matrix[i][j]:.1f} ", end="")
    print()
