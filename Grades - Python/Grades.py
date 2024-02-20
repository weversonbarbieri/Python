firstgrade: float
secondgrade: float

firstgrade = float(input("Enter the 1st grade: "))
secondgrade = float(input("Enter the 2nd grade: "))

finalgrade = firstgrade + secondgrade

if finalgrade > 60:
    print(f"FINAL GRADE = {finalgrade:.1F}")
else:
    print("NOT APPROVED")