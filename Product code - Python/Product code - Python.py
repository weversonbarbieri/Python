code: float; total: float
quantity: int


code = int(input("Enter the product code: "))
quantity = int(input("Quantity purchased: "))

if code == 1:
    total = quantity * 5.00
    print(f"Dued value: $ {total:.2f}")
elif code == 2:
    total = quantity * 3.50
    print(f"Dued value: $ {total:.2f}")
elif code == 3:
    total = quantity * 4.80
    print(f"Dued value: $ {total:.2f}")
elif code == 4:
    total = quantity * 8.90
    print(f"Dued value: $ {total:.2f}")
elif code == 5:
    total = quantity * 7.32
    print(f"Dued value: $ {total:.2f}")



