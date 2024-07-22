import random

hotFlavors = {
    "espresso": {"cost": 1.50, "ingredients": {"water": 50, "milk": None, "coffee": 18}},
    "latte": {"cost": 2.50, "ingredients": {"water": 200, "milk": 150, "coffee": 24}},
    "cappuccino": {"cost": 3.00, "ingredients": {"water": 250, "milk": 100, "coffee": 24}}
    }

coffeMachine = {
    "report": {"money": 0.00, "ingredients": {"water": 300, "milk": 200, "coffee": 100}}
    }

coffeRefill = {
    "water": 300,
    "milk": 200,
    "coffee": 100
    }

def GetSpecificData(coffeType):
    if(coffeType not in hotFlavors):
        water = coffeMachine['report']['ingredients']['water']
        milk = coffeMachine['report']['ingredients']['milk']
        coffe = coffeMachine['report']['ingredients']['coffee']
        money = coffeMachine['report']['money']
    else:
        water = hotFlavors[coffeType]['ingredients']['water']
        milk = hotFlavors[coffeType]['ingredients']['milk']
        coffe = hotFlavors[coffeType]['ingredients']['coffee']
        money = hotFlavors[coffeType]['cost']
    return money, water, milk, coffe


def PutSpecificData(coffeType, money, water, milk, coffe):
    if(coffeType not in hotFlavors):
        coffeMachine['report']['ingredients']['water'] = water 
        coffeMachine['report']['ingredients']['milk'] = milk 
        coffeMachine['report']['ingredients']['coffee'] = coffe
        coffeMachine['report']['money'] = money
    else:
        hotFlavors[coffeType]['ingredients']['water'] = water
        hotFlavors[coffeType]['ingredients']['milk'] = milk
        hotFlavors[coffeType]['ingredients']['coffee'] = coffe
        hotFlavors[coffeType]['cost'] = money
        
def UpdateSpecificData(coffeType, money, water, milk, coffe):
    
    currentMoney, currentWater, currentMilk, currentCoffe = GetSpecificData(coffeType)

    water = water if water != None else currentWater
    milk = milk if milk != None else currentMilk
    coffe = coffe if coffe != None else currentCoffe
    money = money if money != None else currentMoney
    
    PutSpecificData(coffeType, money, water, milk, coffe)
    

def AddSpecificData(coffeType, money, water, milk, coffe):
    
    currentMoney, currentWater, currentMilk, currentCoffe = GetSpecificData(coffeType)

    water = water + currentWater if (water != None and currentWater != None) else currentWater
    milk = milk + currentMilk if (milk != None and currentMilk != None) else currentMilk
    coffe = coffe + currentCoffe if (coffe != None and currentCoffe != None) else currentCoffe
    money = money + currentMoney if (money != None and currentMoney != None) else currentMoney
    
    PutSpecificData(coffeType, money, water, milk, coffe)
           
def DifferenceBetweenIngredients(coffeType):
    moneyReport, waterReport, milkReport, coffeReport = GetSpecificData("report")
    currentMoney, currentWater, currentMilk, currentCoffe = GetSpecificData(coffeType)
    
    diffWater = waterReport - currentWater if (waterReport != None and currentWater != None) else None
    diffMilk  = milkReport - currentMilk   if (milkReport  != None and currentMilk  != None) else None
    diffCoffe = coffeReport - currentCoffe if (coffeReport != None and currentCoffe != None) else None
    
    return diffWater, diffMilk, diffCoffe 

def PrintReport():
    money, water, milk, coffe = GetSpecificData("report")
    print(f"Water: {water}ml\nMilk: {milk}ml\nCoffee: {coffe}g\nMoney: ${money}")
    

def CheckIngredients(coffeType):
    returnCode = True
    water, milk, coffe = DifferenceBetweenIngredients(coffeType)
    differences = [water, milk, coffe]       
    for item in differences:
        if(water != None):
            if water < 0:
                print(f"Sorry there is not enough {item} to make that flavor.")
                returnCode = False  
    return returnCode

def DispatchCoffee(coffeType):
    moneyReport, waterReport, milkReport, coffeReport = GetSpecificData("report")
    currentMoney, currentWater, currentMilk, currentCoffe = GetSpecificData(coffeType)
    
    water = waterReport - currentWater if (waterReport != None and currentWater != None) else waterReport
    milk = milkReport - currentMilk   if (milkReport  != None and currentMilk  != None) else milkReport
    coffe = coffeReport - currentCoffe if (coffeReport != None and currentCoffe != None) else coffeReport
    money = moneyReport + currentMoney if (moneyReport != None and currentMoney != None) else moneyReport
    
    PutSpecificData("report", money, water, milk, coffe)

def DeliverCoffer(coffeType):
    isAvailable = CheckIngredients(coffeType)
    if isAvailable:
        DispatchCoffee(coffeType)
        print(f"Here is your {coffeType}. Enjoy!")
    else:
        PrintReport()
        print("Sorry, there is not enough ingredients to make that flavor. Please try again later.")

def GetCashInCoins(coffeType):
    money = GetSpecificData(coffeType)[0]
    cash = round(money, 2)
    totalReceived = 0
    left = cash
    while(left > 0):
        quarters = 0
        dimes = 0
        nickels = 0
        pennies = 0
        try:
            quarters = int(input("How many quarters?: "))
        except:
            print(f"Next time, please enter a valid number of quarters. it is considered as 0")
        try:
            dimes = int(input("How many dimes?: "))
        except:
            print(f"Next time, please enter a valid number of dimes. it is considered as 0")
        try:
            nickels = int(input("How many nickels?: "))
        except:
            print(f"Next time, please enter a valid number of nickels. it is considered as 0")
        try:
            pennies = int(input("How many pennies?: "))
        except:
            print(f"Next time, please enter a valid number of pennies. it is considered as 0")
        quartersMoney = round(quarters * 0.25, 2)
        dimesMoney = round(dimes * 0.10, 2)
        nickelsMoney = round(nickels * 0.05, 2)
        penniesMoney = round(pennies * 0.01, 2)
        received = round(quartersMoney + dimesMoney + nickelsMoney + penniesMoney, 2)
        if(received <= 0):
            break
        totalReceived += round(quartersMoney + dimesMoney + nickelsMoney + penniesMoney, 2)
        left = round(cash - totalReceived, 2)
        if(left > 0):
            print(f"Sorry, that's not enough money. Please insert ${left} more.")
    return totalReceived

def calculateChange(coffeType, cash):
    money = GetSpecificData(coffeType)[0]
    diff = round(cash - money, 2)
    change = cash
    if diff < 0:
        print(f"Sorry, that's not enough money. Money refunded. ${change}")
    else:
        print(f"Here is ${change} in change.")
        change = diff
    
    return change

def MachineRefill():
    UpdateSpecificData("report", 0.00, coffeRefill['water'], coffeRefill['milk'], coffeRefill['coffee'])
    print("The machine has been refilled.")

def main():
    # Your code here
    print("Welcome to the Coffee Machine!")
    running = True
    while True == running:
        coffeType = input("What would you like? (espresso/latte/cappuccino): ")
        coffeType = coffeType.lower()
        if(coffeType == "report"):
           PrintReport()
        elif(coffeType == "refill"):
            MachineRefill()
        elif(coffeType == "off"):
            running = False
        elif coffeType in hotFlavors:
            cash = GetCashInCoins(coffeType)
            change = calculateChange(coffeType, cash)
            if change != cash:
                DeliverCoffer(coffeType)
        else:
            print("Sorry, we don't have that flavor.")

if __name__ == "__main__":
    main()