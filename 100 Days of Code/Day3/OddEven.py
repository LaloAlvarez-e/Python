
def main():
    #get user input
    number = input("Which number do you want to check? ")
    #check if the number is even or odd
    try:
        number = int(number)
        if number % 2 == 0:
            print("This is an even number.")
        else:
            print("This is an odd number.")
    except ValueError:
        print("Invalid input. Please enter a number.")
        return
 
if __name__ == "__main__":
    main()