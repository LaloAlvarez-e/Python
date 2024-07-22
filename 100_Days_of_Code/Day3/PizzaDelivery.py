#create a main function
def main():
    #get user input
    print ("Thanks for choosing the Pizza Delivery!")
    size = input("What size pizza do you want? S, M, or L ")
    addPepperoni = input("Do you want pepperoni? Y or N ")
    extraCheese = input("Do you want extra cheese? Y or N ")
    #calculate the bill
    bill = 0
    size = size.upper()
    sizeChar = size[0]
    if sizeChar == 'S':
        bill = 15
    elif sizeChar == 'M':
        bill = 20
    else:
        bill = 25

    addPepperoni = addPepperoni.upper()
    addPepperoniChar = addPepperoni[0]
    if addPepperoniChar == 'Y':
        if size == 'S':
            bill += 2
        else:
            bill += 3
            
    extraCheese = extraCheese.upper()
    extraCheeseChar = extraCheese[0]
    if extraCheeseChar == 'Y':
        bill += 1
    print(f"Your final bill is: ${bill}.")
    
if __name__ == "__main__":
    main()