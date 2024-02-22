salary: float; newsalary: float; increasevalue: float
percentage1: int; percentage2: int; percentage3: int; percentage4: int

percentage1 = 20
percentage2 = 15
percentage3 = 10
percentage4 = 5
salary = float(input("Enter the salary: "))

if salary <= 1000:
    increasevalue = (salary * percentage1) / 100
    newsalary = increasevalue + salary
    print(f"New salary = $ {newsalary:.2f}")
    print(f"Increased value: {increasevalue:.2f}")
    print(f"Percentage = {percentage1} %")
elif salary > 1000 and salary < 3000:
    increasevalue = (salary * percentage2) / 100
    newsalary = increasevalue + salary
    print(f"New salary = $ {newsalary:.2f}")
    print(f"Increased value: {increasevalue:.2f}")
    print(f"Percentage = {percentage2} %")
elif salary > 3000 and salary <= 8000:
    increasevalue = (salary * percentage3) / 100
    newsalary = increasevalue + salary
    print(f"New salary = $ {newsalary:.2f}")
    print(f"Increased value: {increasevalue:.2f}")
    print(f"Percentage = {percentage3} %")
else:
    increasevalue = (salary * percentage4) / 100
    newsalary = increasevalue + salary
    print(f"New salary = $ {newsalary:.2f}")
    print(f"Increased value: {increasevalue:.2f}")
    print(f"Percentage = {percentage4}")
