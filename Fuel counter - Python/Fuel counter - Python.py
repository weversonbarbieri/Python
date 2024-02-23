fuelcode: int; sumdiesel: int; sumgasoline: int; sumalcohool: int

fuelcode = int(input("Enter the fuel code (1, 2, 3) or for to stop: "))

sumalcohool = 0
sumgasoline = 0
sumdiesel = 0

while fuelcode != 4:
    if fuelcode == 1:
        sumalcohool = sumalcohool + 1
    elif fuelcode == 2:
        sumgasoline = sumgasoline + 1
    elif fuelcode == 3:
        sumdiesel = sumdiesel + 1
    fuelcode = int(input("Enter the fuel code (1, 2, 3) or for to stop: "))

print("THANK YOU")

print("Alcohool: ", sumalcohool)
print("Gasoline = ", sumgasoline)
print("Diesel", sumdiesel)