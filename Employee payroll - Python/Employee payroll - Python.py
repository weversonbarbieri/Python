
name = str(input("Name: "))
hourlyrate = float(input("Hourly rate: "))
workedhours = int(input("Worked hours: "))

payroll = hourlyrate * workedhours

print(f"The payroll for {name} should be {payroll:.2f}.")