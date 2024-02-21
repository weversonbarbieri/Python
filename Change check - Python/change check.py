price: float; money: float; change: float; total: float; change: float
quantity: int

price = float(input("Product price: "))
quantity = int(input("Quantity purchased: "))
money = float(input("Money received: "))

total = price * quantity

if money < total:
    change = total - money
    print(f"NOT ENOUGH MONEY. MISSING $ {change:.2f}")
else:
    change = total - money
    print(f"CHANGE = {change:.2f}")