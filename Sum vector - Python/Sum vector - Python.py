
N = int(input("How many values will have each vector? "))

vectorA = [0 for x in range(N)]
vectorB = [0 for x in range(N)]
vectorsum = [0 for x in range(N)]

print("Enter the vector A values: ")
for i in range(0, N):
    vectorA[i] = int(input())

print("Enter the vector B values: ")
for i in range(0, N):
    vectorB[i] = int(input())


for i in range(0, N):
    vectorsum[i] = vectorA[i] + vectorB[i]

print("VECTOR RESULT:")
for i in range(0, N):
    print(vectorsum[i])
