sumgrades: float

N = int(input("How many students do you want to type? "))

vectorname = [0 for x in range(N)]
vectorgrade1 = [0 for x in range(N)]
vectorgrade2 = [0 for x in range(N)]
vectorfinalgrade = [0 for x in range(N)]

for i in range(0, N):
    print(f"Enter the name, first grade and second grade of the {i + 1}o studant:")
    vectorname[i] = str(input())
    vectorgrade1[i] = float(input())
    vectorgrade2[i] = float(input())

for i in range(0, N):
    vectorfinalgrade[i] = (vectorgrade1[i] + vectorgrade2[i]) / 2

print("Approved students:")
for i in range(0, N):
    if vectorfinalgrade[i] >= 6:
        print(f"{vectorname[i]}")




