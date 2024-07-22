#create main function  
def main():
    #get user input
    year = input("Which year do you want to check? ")
    #check if the year is a leap year
    try:
        year = int(year)
        isLeap = False
        if (year % 4 == 0):
            isLeap = True
            if (year % 100 == 0) and (year % 400 != 0):
                isLeap = False
        if(isLeap != False):
            print("Leap year")
        else:
            print("Not leap year")
    except ValueError:
        print("Invalid input. Please enter a number.")
        return
#call the main function
if __name__ == "__main__":
    main()