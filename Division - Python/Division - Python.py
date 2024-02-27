numerator: int
denominator: int
divisionresult: float

N = int(input("How many cases do want to type? "))

for i in range(0, N):
    numerator = int(input("Enter the numerator: "))
    denominator = int(input("Enter the denominator: "))
    if denominator == 0:
        print("DIVISION NOT POSSIBLE")
    else:
        divisionresult = numerator / denominator
        print(f"DIVISION RESULT = {divisionresult:.2f}")
