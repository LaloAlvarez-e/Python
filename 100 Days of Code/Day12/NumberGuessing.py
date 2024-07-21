import random

def GuessLogo():
    print('''  
               _  __           __             _____                 _          
              / |/ /_ ____ _  / /  ___ ____  / ___/_ _____ ___ ___ (_)__  ___ _
             /    / // /  ' \\/ _ \\/ -_) __/ / (_ / // / -_|_-<(_-</ / _ \\/ _ `/
            /_/|_/\\_,_/_/_/_/_.__/\\__/_/    \\___/\\_,_/\\__/___/___/_/_//_/\\_, / 
                                                                        /___/   
                    ''')
def main():
    GuessLogo()
    randomNumber = random.randint(1, 100)
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")
    difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ")
    difficulty = difficulty.lower()
    attempts = 10 if difficulty == "easy" else 5
    running = True
    while((True == running) and (0 < attempts)):
        guessNumber = input("Make a guess: ")
        try:
            guess = int(guessNumber)
            diff = abs(randomNumber - guess)
            if(diff == 0):
                print(f"You got it! The answer was {randomNumber}.")
                running = False
            elif(diff <= 10):
                print("Close, but no cigar.")
            elif(diff <= 20):
                print("You're a bit far.")
            elif(diff <= 30):
                print("You're far.")
            elif(diff <= 40):
                print("You're very far.")
            else:
                print("You're very very far.")
            attempts -= 1
            if((True == running) and (0 < attempts)):
                print("Guess again.")
        except ValueError:
            print("Please enter a number.")
            continue
    
    if(0 == attempts):
        print(f"You've run out of attempts. The answer was {randomNumber}")

if __name__ == "__main__":
    main()