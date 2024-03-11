profit1020: int
profit20: int
profit10: int
sumpurchased: float
sumsold: float
totalprofit: float
profitpercentage: float

N = int(input("How many products data will be entered? "))

vectorproductname = [0 for x in range(N)]
vectorpurchasedprince = [0 for x in range(N)]
vectorpricesold = [0 for x in range(N)]
vectorprofit = [0 for x in range(N)]

for i in range(0, N):
    vectorproductname[i] = str(input("Name: "))
    vectorpurchasedprince[i] = float(input("Purchased price: "))
    vectorpricesold[i] = float(input("Sold price: "))

sumpurchased = 0
sumsold = 0
for i in range(0, N):
    sumpurchased = sumpurchased + vectorpurchasedprince[i]
    sumsold = sumsold + vectorpricesold[i]

profit1020 = 0
profit20 = 0
profit10 = 0
for i in range(0, N):
    vectorprofit[i] = vectorpricesold[i] - vectorpurchasedprince[i]
    profitpercentage = (vectorprofit[i] * 100) / vectorpricesold[i]
    if profitpercentage < 10:
        profit10 = profit10 + 1
    elif profitpercentage >= 10 and profitpercentage <= 20:
        profit1020 = profit1020 + 1
    else:
        profit20 = profit20 + 1

totalprofit = sumsold - sumpurchased
print()
print("REPORT:")
print(f"Profit < 10%: {profit10}")
print(f"Profit between 10% and 20%: {profit1020}")
print(f"Profit > 20%: {profit20}")
print(f"Total purchased: {sumpurchased:.2f}")
print(f"Total sold: {sumsold:.2f}")
print(f"Total profit: {totalprofit:.2f}")