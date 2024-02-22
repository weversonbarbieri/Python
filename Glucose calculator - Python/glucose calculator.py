glucose: float

glucose = float(input("Enter the glucose value: "))

if glucose <= 100:
    print("Classification: normal")
elif glucose > 100 and glucose <= 140:
    print("Classification: elevated")
else:
    print("Classification: diabetes")
