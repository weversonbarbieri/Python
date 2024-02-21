minutes: int
total: float; franchisevalue: float

minutes = int(input("Enter minutes spent: "))

franchisevalue = 50.00
if minutes > 100:
    total = ((minutes - 100) * 2) + franchisevalue
    print(f"Dued value: {total:.2f}")
else:
    print(f"Dued value: {franchisevalue:.2f}")