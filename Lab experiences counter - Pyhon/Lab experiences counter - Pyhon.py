sumfrogs: int
sumrabbits: int
summouses: int
animalsquantity: int
percentagefrogs: float
percentagerabbits: float
percentagemouses: float
animaltype: str

N = int(input("How many tests cases do want to enter? "))

sumfrogs = 0
sumrabbits = 0
summouses = 0
sumanimals = 0
for i in range(0, N):
    animalsquantity = int(input("Animals quantity: "))
    animaltype = str(input("Animal type: "))
    sumanimals = sumanimals + animalsquantity
    if animaltype == 'F':
        sumfrogs = sumfrogs + animalsquantity
    elif animaltype == 'R':
        sumrabbits = sumrabbits + animalsquantity
    elif animaltype == 'M':
        summouses = summouses + animalsquantity


percentagefrogs = (sumfrogs * 100) / sumanimals
percentagerabbits = (sumrabbits * 100) / sumanimals
percentagemouses = (summouses * 100) / sumanimals

print("FINAL REPORT:")
print(f"Total: {sumanimals}")
print(f"Total rabbits: {sumrabbits}")
print(f"Total mouses: {summouses}")
print(f"Total frogs: {sumfrogs}")
print(f"Percentage rabbits: {percentagerabbits:.2f}")
print(f"Percentage mouses: {percentagemouses:.2f}")
print(f"Percentage frogs: {percentagefrogs:.2f}")
