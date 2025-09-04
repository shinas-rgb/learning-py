year = int(input("Enter a year to check if it is a leap year\n"))

if(year % 4 == 0):
    if(year % 100 != 0):
        print("Year is leap year")
    else:
        if(year % 400 == 0):
            print("year is leap year")
        else:
            print("year is not leap year")
        
else:
    print("year is not leap year")
    
