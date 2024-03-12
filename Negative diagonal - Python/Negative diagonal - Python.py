negative: int

N = int(input("Which is the matrix order? "))

matrix = [[0 for x in range(N)] for x in range(N)]

for i in range(0, N):
    for j in range(0, N):
        matrix[i][j] = int(input(f"Element[{i},{j}]: "))

print("MAIN DIAGONAL:")
for i in range(0, N):
    print(f"{matrix[i][i]} ", end="")
print()

negative = 0
for i in range(0, N):
    for j in range(0, N):
        if matrix[i][j] < 0:
            negative = negative + 1

print(f"NEGATIVE QUANTITY = {negative}")