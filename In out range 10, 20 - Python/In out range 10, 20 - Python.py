sumin: int
sumout: int
x: int

N = int(input("How many numbers do want to type? "))
sumin = 0
sumout = 0
for i in range(0, N):
    x = int(input("Enter 1 number: "))
    if x >= 10 and x <= 20:
        sumin = sumin + 1
    else:
        sumout = sumout + 1

print(f"{sumin} IN BETWEEN RANGE 10 - 20.")
print(f"{sumout} OUT BETWEEN RANGE 10 - 20.")