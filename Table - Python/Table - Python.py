table: int

N = int(input("Which number do you want to see the table? "))

for i in range(1, 11):
    table = N * i
    print(f"{N} x {i} = {table}")