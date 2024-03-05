sumevens: int

N = int(input("How many numbers do want to type? "))

vector = [0 for x in range(N)]

for i in range(0, N):
    vector[i] = int(input("Enter 1 numbers: "))

sumevens = 0
print()
print("EVEN NUMBERS:")
for i in range(0, N):
    if vector[i] % 2 == 0:
        sumevens = sumevens + 1
        print(f"{vector[i]} ", end="")

print()
print()
print(f"EVEN QUANTITY = {sumevens}")