greaternumber: int

N = int(input("Which is the matrix order? "))

matrix = [[0 for x in range(N)] for x in range(N)]

for i in range(0, N):
    for j in range(0, N):
        matrix[i][j] = int(input(f"Elemento [{i},{j}]: "))

print("GREATER NUMBER EACH LINE:")
for i in range(0, N):
    greaternumber = matrix[i][j]
    for j in range(0, N):
        if matrix[i][j] > greaternumber:
            greaternumber = matrix[i][j]

    print(f"{greaternumber}")
