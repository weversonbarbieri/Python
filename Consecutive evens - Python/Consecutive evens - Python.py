sumevens: int; x: int

x = int(input("Enter an integer number: "))

while x != 0:
    if (x % 2 == 0):
        sumevens = x + (x + 2) + (x + 4) + (x + 6) + (x + 8)
        print(f"SUM = {sumevens}")
    else:
        sumevens = (x + 1) + (x + 3) + (x + 5) + (x + 7) + (x + 9)
        print(f"SUM = {sumevens}")

    x = int(input("Enter an integer number: "))
