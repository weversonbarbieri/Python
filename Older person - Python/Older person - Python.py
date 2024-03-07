older: int
oldername: str

N = int(input("How many people do want to type? "))

vectorname = [0 for x in range(N)]
vectorage = [0 for x in range(N)]

for i in range(0, N):
    print(f"Enter the data of the {i + 1}a person.")
    vectorname[i] = str(input("Name: "))
    vectorage[i] = int(input("Age: "))

older = vectorage[i]
for i in range(0, N):
    if vectorage[i] > older:
        older = vectorage[i]
        oldername = vectorname[i]

print(f"OLDER PERSON: {oldername}")