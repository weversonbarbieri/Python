x: int; y: int

print("Enter the graph coordenates X and Y:")
x = int(input())
y = int(input())

while x != 0 and y != 0:
    if x > 0 and y > 0:
        print("QUADRANTE Q1")
    elif x < 0 and y > 0:
        print("QUADRANTE Q2")
    elif x < 0 and y < 0:
        print("QUADRANTE Q3")
    elif x > 0 and y < 0:
        print("QUADRANTE Q4")
    print("Enter the graph coordenates X and Y:")
    x = int(input())
    y = int(input())