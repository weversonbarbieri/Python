temperature: str
celsious: float
fahrenheit: float

temperature = str(input("Which temperature do want to calculate(C/F)? "))

if temperature == 'F':
    fahrenheit = float(input("Enter the temperature in Fahrenheit: "))
    celsious = (fahrenheit - 32) / 1.8
    print(f"The equivalent temperature in Celsius is: {celsious:.2f}")
else:
    celsious = float(input("Enter the temperature in Celsius: "))
    fahrenheit = (celsious * 1.8) + 32
    print(f"The equivalent temperature in Fahrenheit is: {fahrenheit:.2f}")


