width: float; length: float; m2price: float; area: float; totalprice: float

width = float(input("Enter the area width: "))
length = float(input("Enter the area length: "))
m2price = float(input("Enter the price per m2: "))

area = width * length
totalprice = area * m2price

print(f"Area = {area:.2f}")
print(f"Total price of the are = {totalprice:.2f}")
