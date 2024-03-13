sum: int

N = int(input("Which is the matrix order? "))

matrix = [[0 for x in range(N)] for x in range(N)]

for i in range(0, N):
    for j in range(0, N):
        matrix[i][j] = int(input(f"Elemento [{i},{j}]: "))

sum = 0
for i in range(0, N):
    for j in range(i + 1, N):
        sum = sum + matrix[i][j]


print(f"The sum of the elements above the main diagonal = {sum}")



