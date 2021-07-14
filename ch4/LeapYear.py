year = eval(input("Enter a Year to check if it's a leap year \n"))
isLeapYear = (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)

if isLeapYear:
    print(year, " is a Leap Year", isLeapYear)

else:
    print(year, " is not a Leap Year")

print(isLeapYear)