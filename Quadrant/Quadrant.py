x: float; y: float

x = float(input("Enter X value: "))
y = float(input("Enter Y value: "))

if x > 0 and y > 0:
    print("Q1")
elif x < 0 and y > 0:
    print("Q2")
elif x < 0 and y < 0:
    print("Q3")
elif x > 0 and y < 0:
    print("Q4")
elif x > 0 and y == 0:
    print("Axle X")
else:
    print("Origem")