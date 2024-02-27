x: int

N = int(input("How many numbers do want to type? "))

for i in range(0, N):
    x = int(input("Enter 1 number: "))
    if x > 0 and x % 2 == 0:
        print("POSITIVE ODD")
    elif x < 0 and x % 2 == 0:
        print("NEGATIVE ODD")
    elif x > 0 and x % 2 != 0:
        print("POSITIVE EVEN")
    elif x < 0 and x % 2 != 0:
        print("NEGATIVE EVEN")
    else:
        print("NULL")

