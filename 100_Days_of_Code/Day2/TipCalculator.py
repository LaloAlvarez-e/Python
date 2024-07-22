def main():
    print("Welcome to the tip calculator.")
    totalBillInput = input("What was the total bill? $")
    tipInput = input("How much tip would you like to give? 10%, 12%, or 15%? ")
    splitNuberInput = input("How many people to split the bill? ")
    totalBill = None
    tipNumber = None
    splitNumber = None
    try: 
        totalBill = float(totalBillInput)
        tipNumber = int(tipInput)
        splitNumber = int(splitNuberInput)
        
        costPerPerson = (totalBill *(1 + (tipNumber / 100))) / splitNumber
        costPerPerson = round(costPerPerson, 2)
        print("Each person should pay: ${:.2f}".format(costPerPerson))
    except ValueError:
        totalBillOutput = totalBillInput if totalBill is None else totalBill
        tipOutput =splitNuberInput if tipNumber is None else tipNumber
        splitNumberOutput = splitNuberInput if splitNumber is None else splitNumber
        print("Invalid input. Total Bill: "+ totalBillOutput +" Tip: "+ tipOutput + " Split Number: "+ splitNumberOutput)   
        return
    

if __name__ == "__main__":
    main()