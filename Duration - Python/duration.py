
seconds = int(input("Enter the duration in seconds: "))

seconds1 = seconds / 60
seconds2 = seconds // 60
totalseconds = (seconds1 - seconds2) * 60

minutes1 = seconds2 / 60
minutes2 = seconds2 // 60

totalminutes = (minutes1 - minutes2) * 60

print(f"{minutes2}:{totalminutes:.0f}:{totalseconds:.0f}")



