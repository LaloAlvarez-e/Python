#create main function 

def IsLeapYear(year):
    isLeap = False
    if(type(year) == int):
        if ((year % 4 == 0) and (year > 0)) :
            isLeap = True
            if (year % 100 == 0) and (year % 400 != 0):
                isLeap = False
    return isLeap

def DaysInMonth(year, month):
    daysInMonth = 0
    if(type(year) == int) and (type(month) == int):
        if(month >= 1) and (month <= 12):
            if month == 2:
                isLeap = IsLeapYear(year)
                daysInMonth = 29 if isLeap else 28
            elif (month == 4) or (month == 6) or (month == 9) or (month == 11):
                daysInMonth = 30
            else:
                daysInMonth = 31
    return daysInMonth

def DaysInMonth1(year, month):
    monthDays = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31] 
    daysInMonth = 0
    if(type(year) == int) and (type(month) == int):
        if(month >= 1) and (month <= 12):
            isLeap = IsLeapYear(year)
            if (month == 2) and (isLeap):
                daysInMonth = 29
            else:
                daysInMonth = monthDays[month - 1]
    return daysInMonth
 
def main():
    #get user input
    year = input("Which year do you want to check? ")
    month = input("Which month do you want to check? ")
    #check if the year is a leap year
    try:
        year = int(year)
        month = int(month)
        daysInMonth = DaysInMonth(year, month)
        print(daysInMonth)
    except ValueError:
        print("Invalid input. Please enter a number.")
        return
#call the main function
if __name__ == "__main__":
    main()