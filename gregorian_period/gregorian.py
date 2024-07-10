def gregorian(year):
    if year < 1582 :
        print("Not within Gregorian calender period.")
    elif year % 4 != 0:
        print("Common year")
    elif year % 100 != 0:
        print("Leap year")
    elif year % 400 != 0:
        print("Common year")
    else:
        print("Leap year")

year = int(input("Enter the year : "))
conclusion = gregorian(year)
print(conclusion)