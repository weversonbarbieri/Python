x: int; y: int

print("Enter 2 numbers: ")
x = int(input())
y = int(input())



while x != y:
    if x < y:
        print("INCREASING!")
    else:
        print("DECREASING!")
    print("Enter more 2 numbers: ")
    x = int(input())
    y = int(input())




