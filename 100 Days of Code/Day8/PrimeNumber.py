def IsPrimeNumber(number):
    returnCode = True
    if(type(number) != int):
        returnCode = False
    if (number < 2) and (True == returnCode):
        returnCode = False
    if(True == returnCode):
        for i in range(2, number):
            if number % i == 0:
                returnCode = False
                break
    return returnCode

def main():
    # Your code here
    numbertoCheck = input("Check this number: ")
    try:
        numbertoCheck = int(numbertoCheck)
        isPrime = IsPrimeNumber(numbertoCheck)
        result = " " if (True == isPrime) else " not "    
        print(f"It's{result}a prime number.")
    except ValueError:
        print("Invalid input. Please enter a valid number.")
        return

if __name__ == "__main__":
    main()