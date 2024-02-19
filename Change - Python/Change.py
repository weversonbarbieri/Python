

productprice = (float(input("Produtc price: ")))
quantity = (int(input("Quantity purchased: ")))
money = (float(input("Money received: ")))

total = money - (productprice * quantity)

print(f"CHANGE = {total:.2f}")
