#create main function
def main():
    #get user input
    print ("Welcome to the rollercoaster!")
    height = input("What is your height in cm? ")
    #check if the user is eligible for a rollercoaster ride
    try:
        height = int(height)
        if height >= 120:
            print("You can ride the rollercoaster.")
            age = input("What is your age? ")
            age = int(age)
            bill = 0
            auxiliarString  = None
            if age <= 12:
                bill = 5
                auxiliarString = "Child"
            elif age <= 18:
                bill = 7
                auxiliarString = "Youth"
            else:
                bill = 12
                auxiliarString = "Adult"
            print(f"{auxiliarString}, Please pay ${bill}.")
            
            takePhoto = input("Do you want a photo taken? Y or N ")
            takePhotoChar = takePhoto[0].upper()
            if takePhotoChar == 'Y':
                bill += 3
                print("Photo taken.")
            else:
                print("No photo taken.")
            print(f"Your total bill is ${bill}.")
        else:
            print("Sorry, you have to grow taller before you can ride.")
    except ValueError:
        print("Invalid input. Please enter a valid number.")
        return

if __name__ == "__main__":
    main()