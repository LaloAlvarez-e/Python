class CoffeMachine:

    def __init__(self, cash=0, water=300, milk=200, coffee=100):
        self.initialResources = {
            "cash": cash,
            "water": water,
            "milk": milk,
            "coffee": coffee,
        }
        self.resources = self.initialResources

    def GetDataResources(self):
        resources = self.resources
        return resources
    
    def PutDataResources(self, resources):
        self.resources = resources
     
    def UpdateDataResources(self, coffeType,resources):
        currentResources = coffeType.GetDataResources(coffeType)
        updateResources = {}
        for key in currentResources:
            updateResources[key] = resources[key] if resources[key] != None else currentResources[key]
        self.PutDataResources(updateResources)
                       
    def DifferenceBetweenIngredients(self, coffeType):
        resources = self.GetDataResources()
        coffeResources = coffeType.GetDataResources()
        diffResources = {}
        for key in resources:
            diffResources[key] = resources[key] - coffeResources[key] if (resources[key] != None and coffeResources[key] != None) else None
        
        return diffResources

    def PrintReport(self):
        resources = self.GetDataResources()
        for key in resources:
            value = resources[key]
            valueString = f"{value}"
            if(key == 'cash'):
                valueString = f"${value}"
            elif(key == "water" or key == "milk"):
                valueString = f"{value}ml"
            elif(key == "coffee"):
                valueString = f"{value}g"
            print(f"{key}: {value}")

    def CheckIngredients(self, coffeType):
        returnCode = True
        differences = self.DifferenceBetweenIngredients(coffeType)        
        for key in differences:
            value = differences[key]
            if(value != None and key != "cash"):
                if value < 0:
                    print(f"Sorry there is not enough {key} to make that flavor.")
                    returnCode = False  
        return returnCode
    
    def DispatchCoffee(self, coffeType):
        differences = self.DifferenceBetweenIngredients(coffeType)
        differences['cash'] = self.GetDataResources()['cash'] + coffeType.GetDataResources()['cash']
        self.PutDataResources(differences)

    def DeliverCoffer(self, coffeType):
        isAvailable = self.CheckIngredients(coffeType)
        if isAvailable:
            self.DispatchCoffee(coffeType)
            print(f"Here is your {coffeType.GetName()}. Enjoy!")
        else:
            self.PrintReport()
            print("Sorry, there is not enough ingredients to make that flavor. Please try again later.")

    def GetCashInCoins(self, coffeType):
        resources = coffeType.GetDataResources()
        money = resources['cash']
        cash = round(money, 2)
        totalReceived = 0
        left = cash
        coins = {"quarters": [0, 0.25, 0], 
                 "dimes":    [0, 0.10, 0], 
                 "nickels":  [0, 0.05, 0], 
                 "pennies":  [0, 0.01, 0]} 
        while(left > 0):
            received = 0
            for coin in coins:
                coins[coin][0] = 0
                coins[coin][2] = 0
                try:
                    coins[coin][0] = int(input(f"How many {coin}?: "))
                except:
                    print(f"Next time, please enter a valid number of {coin}. it is considered as 0")
                coins[coin][2] = round(coins[coin][0] * coins[coin][1], 2)
                received += round(coins[coin][2],2)
            if(received <= 0):
                break
            totalReceived += received
            left = round(cash - totalReceived, 2)
            if(left > 0):
                print(f"Sorry, that's not enough money. Please insert ${left} more.")
        return totalReceived
    
    def calculateChange(self, coffeType, cash):
        resources = coffeType.GetDataResources()
        money = resources['cash']
        diff = round(cash - money, 2)
        change = cash
        if diff < 0:
            print(f"Sorry, that's not enough money. Money refunded. ${change}")
        else:
            print(f"Here is ${change} in change.")
            change = diff
        
        return change
    
    def MachineRefill(self):
        self.PutDataResources(self.initialResources)
        print("The machine has been refilled.")

class CoffeType:
    def __init__(self, name, money, water, milk, coffee):
        self.name = name
        self.ingredients = {
            "cash": money,
            "water": water,
            "milk": milk,
            "coffee": coffee,
        }
    
    def GetDataResources(self):
        return self.ingredients
    def GetName(self):
        return self.name
    

def main():
    # Your code here
    coffeCategories = {
        "espresso": CoffeType("espresso", 1.5, 50, 0, 18),
        "latte": CoffeType("latte", 2.5, 200, 150, 24),
        "cappuccino": CoffeType("cappuccino", 3.0, 250, 100, 24)
    }
    coffeMachine = CoffeMachine(0, 300, 200, 100)
    
    # Your code here
    print("Welcome to the Coffee Machine!")
    running = True
    print(F"${coffeCategories.keys()}")
    while True == running:
        coffeType = input("What would you like? (espresso/latte/cappuccino): ")
        coffeType = coffeType.lower()
        if(coffeType == "report"):
           coffeMachine.PrintReport()
        elif(coffeType == "refill"):
            coffeMachine.MachineRefill()
        elif(coffeType == "off"):
            running = False
        elif coffeType in coffeCategories.keys():
            coffeObject = coffeCategories[coffeType]
            cash = coffeMachine.GetCashInCoins(coffeObject)
            change = coffeMachine.calculateChange(coffeObject, cash)
            if change != cash:
                coffeMachine.DeliverCoffer(coffeObject)
        else:
            print("Sorry, we don't have that flavor.")


if __name__ == "__main__":
    main()