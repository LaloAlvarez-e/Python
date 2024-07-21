    
def ExecuteCeasarCipher(text, shift, mode):
    executionText = ""
    alphabetSize = 26
    if(shift > alphabetSize):
        shift = shift % alphabetSize
    if(shift == 0):
        return text
    if(mode == "decode"):
        shift = -shift
    for character in text:
        if character.isalpha():
            asciiValue = ord(character)
            if character.islower():
                extractChar = ord('a')
            else:
                extractChar = ord('A')
            # Convert to 0 based index
            asciiBase = asciiValue -  extractChar 
            # Apply shift, and wrap around if needed, example: z + 1 = a
            shiftValue = (asciiBase + shift) % alphabetSize 
            #convert to origital ascii value
            originalValue =  shiftValue + extractChar
            character = chr(originalValue)
            print(f"asciiValue: {asciiValue} extractChar: {extractChar} asciiBase: {asciiBase} shiftValue: {shiftValue} originalValue: {originalValue} character: {character}")
        executionText += character
    return executionText


def main():
    
    running = True
    while(running):
        cipher = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
        text = input("Type your message: \n")
        shift = input("Type the shift number: \n")
        try:
            shift = int(shift)
        except ValueError:
            print("Invalid input. Please enter a valid number.")
            continue
        
        result = ExecuteCeasarCipher(text, shift, cipher)
        print(f"Here's the {cipher}d result: {result}")
        runningText = input("Do you want to continue? Type 'yes' or 'no':\n") 
        if (runningText != "yes"):
            running = False
    # Your code here

if __name__ == "__main__":
    main()        