starttime: int; endtime: int; dutation: int

starttime = int(input("Enter the started time: "))
endtime = int(input("Enter the started time: "))

if starttime > 12 and endtime < 12:
    duration = (24 - starttime) + endtime
    print(f"The game lasted {duration} hours")
elif starttime < 12 and endtime > 12:
    duration = (12 - starttime) + (endtime - 12)
    print(f"The game lasted {duration} hours")
elif starttime > 12 and endtime > 12:
    duration = (24 - starttime) + endtime
    print(f"The game lasted {duration} hours")
else:
    duration = (12 + starttime) + (12 + endtime)
    print(f"The game lasted {duration}")

