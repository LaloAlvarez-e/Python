def CalculatorLogo():
    print('''
           _____________________
          |  _________________  |
          | | CALCULATOR      | |
          | |_________________| |
          |  ___ ___ ___   ___  |
          | | 7 | 8 | 9 | | + | |
          | |___|___|___| |___| |
          | | 4 | 5 | 6 | | - | |
          | |___|___|___| |___| |
          | | 1 | 2 | 3 | | x | |
          | |___|___|___| |___| |
          | | . | 0 | = | | / | |
          | |___|___|___| |___| |
          |_____________________|
          ''')

def SanityCheck(number,):
    returnCode = False
    if( (type(number)  == float or type(number)  == int)):
        returnCode = True
    return returnCode

def SanityCheck2(firstNumber, secondNumber):
    returnCode = False
    sanityCheck1 = SanityCheck(firstNumber)
    sanityCheck2 = SanityCheck(secondNumber)
    if( True == sanityCheck1) and (True == sanityCheck2):
        returnCode = True
    return returnCode
    
def ConvertTypes(number):
    returnNumber = number
    sanityCheck = SanityCheck(number)
    if(True == sanityCheck):
        numberInt = int(number)
        if(numberInt == number):
            returnNumber = numberInt
    return returnNumber

def ConverTypes3(firstNumber, secondNumber, result):
    returnFirstNumber = ConvertTypes(firstNumber)
    returnSecondNumber = ConvertTypes(secondNumber)
    returnResult = ConvertTypes(result)
    return (returnFirstNumber, returnSecondNumber, returnResult)

def Add2(firstNumber, secondNumber):
    result = None
    sanityCheck = SanityCheck2(firstNumber, secondNumber)
    if( True == sanityCheck):
        result = firstNumber + secondNumber
        (firstNumber, secondNumber, result) = ConverTypes3(firstNumber, secondNumber, result)
    return (firstNumber, secondNumber, result)

def Substract2(firstNumber, secondNumber):
    result = None
    sanityCheck = SanityCheck2(firstNumber, secondNumber)
    if( True == sanityCheck):
        result = firstNumber - secondNumber
        (firstNumber, secondNumber, result) = ConverTypes3(firstNumber, secondNumber, result)
    return (firstNumber, secondNumber, result)

def Multiply2(firstNumber, secondNumber):
    result = None
    sanityCheck = SanityCheck2(firstNumber, secondNumber)
    if( True == sanityCheck):
        result = firstNumber * secondNumber
        (firstNumber, secondNumber, result) = ConverTypes3(firstNumber, secondNumber, result)
    return (firstNumber, secondNumber, result)

def Divide2(firstNumber, secondNumber):
    result = None
    sanityCheck = SanityCheck2(firstNumber, secondNumber)
    if( True == sanityCheck):
        result = firstNumber / secondNumber
        (firstNumber, secondNumber, result) = ConverTypes3(firstNumber, secondNumber, result)
    return (firstNumber, secondNumber, result)

def Module2(firstNumber, secondNumber):
    result = None
    sanityCheck = SanityCheck2(firstNumber, secondNumber)
    if( True == sanityCheck):
        result = firstNumber % secondNumber
        (firstNumber, secondNumber, result) = ConverTypes3(firstNumber, secondNumber, result)
    return (firstNumber, secondNumber, result)

def Power2(firstNumber, secondNumber):
    result = None
    sanityCheck = SanityCheck2(firstNumber, secondNumber)
    if( True == sanityCheck):
        result = firstNumber ** secondNumber
        (firstNumber, secondNumber, result) = ConverTypes3(firstNumber, secondNumber, result)
    return (firstNumber, secondNumber, result)

def InvalidOperation(firstNumber, secondNumber):
    return None
def main():
    # Your code here
    functionMap = {
        "+": Add2, 
        "-": Substract2,
        "*": Multiply2,
        "/": Divide2,
        "^": Power2,
        "%": Module2}
    running = True
    result = 0
    continueOperations = 'n'
    CalculatorLogo()
    while(True == running):
        if(continueOperations != 'y'):
            firstNumber = input("What's the first number?: ")
        else:
            firstNumber = result
        operation = input("Pick an operation: +, -, *, /, ^, %: ")
        secondNumber = input("What's the second number?: ")
        operation = operation[0]
        try:
            firstNumber = float(firstNumber)
            secondNumber = float(secondNumber)
            functionOp = None
            if(operation not in functionMap):
                functionOp = InvalidOperation
            else:   
                functionOp = functionMap[operation]
            
            (firstNumber, secondNumber, result) =  functionOp(firstNumber, secondNumber)
            print(f"{firstNumber} {operation} {secondNumber} = {result}")
        except:
            print("Invalid number, please enter a valid number")
        continueOperations = input("Type 'y' to continue calculating with the result, or 'n' to start a new calculation, or 'e' to exit: ")
        continueOperations = continueOperations.lower()
        if (continueOperations != 'n') and (continueOperations != 'y'):
            running = False
            

if __name__ == "__main__":
    main()