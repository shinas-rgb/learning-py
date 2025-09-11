def days_in_month(year, month):
    month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    is_leap = False
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                is_leap = True
        else:
            is_leap = True
    if is_leap == True and month == 2:
        return month_days[1] + 1
    return month_days[month - 1]

year = int(input("Enter the year: "))
month = int(input("Enter the month(1 - 12): "))

days = days_in_month(year, month)
print(days)
