factorial: int

N = int(input("Enter N value: "))

factorial = 1
for i in range(1, N+1):
    factorial = factorial * i

print(f"FACTORIAL = {factorial}")