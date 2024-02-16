
print("Enter the name of the 1st person.")
name1 = str(input("Name: "))
age1 = int(input("Age: "))

print("Enter the name of the 2st person.")
name2 = str(input("Name: "))
age2 = int(input("Age: "))

average = (age1 + age2) / 2

print(f"The average age of {name1} and {name2} is {average:.1f} years old.")
