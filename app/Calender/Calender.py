def printMonth(year, month):
    printMonthTitle(year, month)
    printMonthBody(year, month)


def printMonthTitle(year, month):
    print("          ", getMonthName(month), " ", year)

    print("—————————————————————————————————————")

    print("  Sun  Mon  Tue  Wed  Thu  Fri  Sat")


def printMonthBody(year, month):
    startDay = getStartDay(year, month)
    numberOfDaysInAMonth = getNumberOfDaysInAMonth(year, month)

    i = 0
    for i in range(0, startDay):
        print("    ", end=" ")
    for i in range(1, numberOfDaysInAMonth + 1):
        print(format(i, "4d"), end=" ")
        if (i + startDay) % 7 == 0:
            print()


def getMonthName(month, monthName="January"):
    if month == 1:
        var = monthName == "January"
    elif month == 2:
        monthName = "February"
    elif month == 3:
        monthName = "March"
    elif month == 4:
        monthName = "April"
    elif month == 5:
        monthName = "May"
    elif month == 6:
        monthName = "June"
    elif month == 7:
        monthName = "July"
    elif month == 8:
        monthName = "August"
    elif month == 9:
        monthName = "September"
    elif month == 10:
        monthName = "October"
    elif month == 11:
        monthName = "November"
    else:
        "December"

    return monthName


def getStartDay(year, month):
    START_DAY_FOR_JANUARY_1_1800 = 3
    totalNumbersOfDays = getTotalNumbersOfDays(year, month)

    return (totalNumbersOfDays + START_DAY_FOR_JANUARY_1_1800) % 7


def getTotalNumbersOfDays(year, month):
    total = 0
    for i in range(1800, year):
        if isLeapYear(i):
            total = total + 366
        else:
            total = total + 365

    for i in range(1, month):
        total = int(total) + getNumberOfDaysInAMonth(year, i)

    return int(total)


def getNumberOfDaysInAMonth(year, month):
    if month == 1 or month == 3 or month == 5 or month == 7 or month == 8 or month == 10 or month == 12:
        return 31
    if month == 4 or month == 6 or month == 9 or month == 11:
        return 30
    if month == 2:
        return 29 if isLeapYear(year) else 28

    if month < 1 and month > 12:
        return print("Invalid Month entered")

    print("getNumberOfDaysInAMonth")


def isLeapYear(year):
    return year % 400 == 0 or (year % 4 == 0 and year % 100 != 0)


def main():
    year = eval(input("Enter a Full Year:\n"))
    month = eval(input("Enter a month as a number between 1 - 12:\n"))
    printMonth(year, month)


main()
