import random

hangman_word = '''
    _    _                                         
 | |  | |                                        
 | |__| | __ _ _ __   __ _ _ __ ___   __ _ _ __  
 |  __  |/ _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
 | |  | | (_| | | | | (_| | | | | | | (_| | | | |
 |_|  |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                                         __/ |                      
                                        |___/                       
'''

hangman_steps = [
    '''
    
    
    
    
    
    
        
    ''',
    '''
    +---+
    |   |
        |
        |
        |
        |
    =========
    ''',
    '''
    +---+
    |   |
    O   |
        |
        |
        |
    =========
    ''',
    '''
    +---+
    |   |
    O   |
    |   |
        |
        |
    =========
    ''',
    '''
    +---+
    |   |
    O   |
   /|   |
        |
        |
    =========
    ''',
    '''
    +---+
    |   |
    O   |
   /|\\  |
        |
        |
    =========
    ''',
    '''
    +---+
    |   |
    O   |
   /|\\  |
   /    |
        |
    =========
    ''',
    '''
    +---+
    |   |
    O   |
   /|\\  |
   / \\  |
        |
    =========
    '''
]

# Your code here

def GetRandomWord(): 
    wordList = ["apple", "banana", "cherry", "date", "elderberry", "fig", "grape", "honeydew", "kiwi", "lemon", "mango", "nectarine", "orange", "papaya", "quince", "raspberry", "strawberry", "tangerine", "watermelon",
                "apricot", "blackberry", "cantaloupe", "dragonfruit", "eggplant", "guava", "huckleberry", "jackfruit", "kumquat", "lime", "mulberry", "olive", "pomegranate", "quince", "rhubarb", "starfruit", "tomato", "ugli fruit",
                "vanilla bean", "wax jambu", "yuzu", "zucchini", "acorn squash", "butternut squash", "cucumber", "delicata squash", "endive", "fennel", "garlic", "hubbard squash", "iceberg lettuce", "jicama", "kale", "leek", "mushroom",
                "napa cabbage", "okra", "parsnip", "quinoa", "radicchio", "spinach", "turnip", "watercress", "yam", "zucchini", "almond", "black bean", "cashew", "date", "edamame", "fava bean", "garbanzo bean", "hazelnut", "italian bean",
                "jackfruit", "kidney bean", "lentil", "mung bean", "navy bean", "oat", "peanut", "quinoa", "rice", "soybean", "tapioca", "udon", "vanilla bean", "wheat", "xanthan gum", "yam", "zucchini", "apple", "banana", "cherry",
                "date", "elderberry", "fig", "grape", "honeydew", "kiwi", "lemon", "mango", "nectarine", "orange", "papaya", "quince", "raspberry", "strawberry", "tangerine", "watermelon", "apricot", "blackberry", "cantaloupe",
                "dragonfruit", "eggplant", "guava", "huckleberry", "jackfruit", "kumquat", "lime", "mulberry", "olive", "pomegranate", "quince", "rhubarb", "starfruit", "tomato", "ugli fruit", "vanilla bean", "wax jambu", "yuzu",
                "zucchini", "acorn squash", "butternut squash", "cucumber", "delicata squash", "endive", "fennel", "garlic", "hubbard squash", "iceberg lettuce", "jicama", "kale", "leek", "mushroom", "napa cabbage", "okra", "parsnip",
                "quinoa", "radicchio", "spinach", "turnip", "watercress", "yam", "zucchini", "almond", "black bean", "cashew", "date", "edamame", "fava bean", "garbanzo bean", "hazelnut", "italian bean", "jackfruit", "kidney bean",
                "lentil", "mung bean", "navy bean", "oat", "peanut", "quinoa", "rice", "soybean", "tapioca", "udon", "vanilla bean", "wheat", "xanthan gum", "yam", "zucchini", "apple", "banana", "cherry", "date", "elderberry", "fig",] 
    return random.choice(wordList)

def CheckCharInWord(word, userWord, char):
    found = False
    alreadyFound = False
    wordLength = len(word)
    if(char in word):
        for i in range(wordLength):
            if(word[i] == char):
                if(userWord[i] == char):
                    alreadyFound = True
                else:
                    userWord[i] = char
                found = True
        
    return (found, alreadyFound)

def PrintCharList(charList):
    for character  in charList:
        if(type(character) == str):
            print(character, end="")
    print("\n")

def HangmanGame(word):
    if(type(word) != str):
        raise ValueError("The word must be a string")
    if(word == ""):
        raise ValueError("The word must not be empty")
    
    wordLength = len(word)
    userWord = ["_"] * wordLength
    maxFailures = len(hangman_steps)
    userFailiures = 0
    
    PrintCharList(userWord)
    while((userFailiures < maxFailures) and ("_" in userWord)):
        userChar = input("Guess a character: ")
        if(len(userChar) != 1):
            print("You must enter a single character")
            continue
        userChar = userChar.lower()
        if(ord(userChar) < ord("a")) or (ord(userChar) > ord("z")):
            print("You must enter a character between a and z")
            continue
        (found, alreadyFound) = CheckCharInWord(word, userWord, userChar)
        if(False == found):
            userFailiures += 1
            print(f"You gessed {userChar}, which is not in the word. You have {maxFailures - userFailiures} attempts left")
        elif(True == alreadyFound):
            print(f"You have already guessed {userChar}. Please try another character")
        PrintCharList(userWord)
        print(f"{hangman_steps[userFailiures]}\n")
            
    if(not "_" in userWord):
        for character  in userWord:
            print(character, end="")
        print("\n")
        print("Congratulations! You have guessed the word")
    else:
        print("Sorry! You have run out of attempts")
        print(f"The word was {word}")
        
            
        
    
    

def main():
    # Your code here
    print(hangman_word)
    randomWord = GetRandomWord()
    HangmanGame(randomWord)
    

if __name__ == "__main__":
    main()