lowerheight: float
higherheight: float
sumheights: float
sumF: int
sumM: int
averageheights: float

N = int(input("How many people will be entered? "))

vectorheights = [0 for x in range(N)]
vectorgenre = [0 for x in range(N)]

for i in range(0, N):
    vectorheights[i] = float(input(f"Enter the height of the {i + 1}a person: "))
    vectorgenre[i] = str(input(f"Enter the genre of the {i + 1}a person: "))

lowerheight = vectorheights[i]
for i in range(0, N):
    if vectorheights[i] < lowerheight:
        lowerheight = vectorheights[i]

higherheight = vectorheights[i]
for i in range(0, N):
    if vectorheights[i] > higherheight:
        higherheight = vectorheights[i]

sumheights = 0
sumF = 0
sumM = 0
for i in range(0, N):
    if vectorgenre[i] == 'F':
        sumheights = sumheights + vectorheights[i]
        sumF = sumF + 1
    else:
        sumM = sumM + 1

averageheights = sumheights / sumF

print(f"Low height = {lowerheight:.2f}")
print(f"Higher height = {higherheight:.2f}")
print(f"Average women height = {averageheights:.2f}")
print(f"Men quantity = {sumM}")