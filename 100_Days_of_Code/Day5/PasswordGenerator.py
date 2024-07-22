import random

listOfLetters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 
                'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 
                'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S',
                'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
listOfSymbols = ['!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '-', '_', '+', '=',
                '{', '}', '[', ']', '|', '\\', ':', ';', '"', "'", '<', '>', ',', '.', 
                '?', '/', '`', '~']
listOfNumbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

def main():
    # Your code here
    print("Welcome to the PyPassword Generator!")
    numberOfLetters = input("How many letters would you like in your password?\n")
    numberOfSymbols = input("How many symbols would you like?\n")
    numberOfNumbers = input("How many numbers would you like?\n")
    
    try:
        numberOfLetters = int(numberOfLetters)
        numberOfSymbols = int(numberOfSymbols)
        numberOfNumbers = int(numberOfNumbers)
        password = ""
        for _ in range(numberOfLetters):
            password += random.choice(listOfLetters)
        for _ in range(numberOfSymbols):
            password += random.choice(listOfSymbols)
        for _ in range(numberOfNumbers):
            password += random.choice(listOfNumbers)
        passwordList = list(password)
        random.shuffle(passwordList)
        password = "".join(passwordList)
        print(f"Your password is: {password}")
    except ValueError:
        print("Invalid input. Please enter a valid number.")
        return

if __name__ == "__main__":
    main()