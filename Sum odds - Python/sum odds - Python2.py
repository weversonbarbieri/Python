sumodds: int
change: int

print("Enter 2 numbers: ")
x = int(input())
y = int(input())

if x > y:
    change = x
    x = y
    y = change

sumodds = 0
for i in range(x+1, y):
    if i % 2 != 0:
        sumodds = sumodds + i

print(f"SUM ODDS: {sumodds}")