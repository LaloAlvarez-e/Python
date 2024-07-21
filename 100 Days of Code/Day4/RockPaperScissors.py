import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
    '''
paper = '''
    _______
---'   ____)____
            ______)
            _______)
            _______)
---.__________)
    '''

scissors = '''
    _______
---'   ____)____
            ______)
        __________)
        (____)
---.__(___)
    '''
    
rock_paper_scissors = [rock, paper, scissors]
def main():
    # Your code here
    print("Welcome to Rock, Paper, Scissors!")
    userChoice = input("What do you choose? Type 0 for Rock, 1 for Paper, or 2 for Scissors.\n")
    try:
        userChoice = int(userChoice)
        if userChoice < 0 or userChoice > 2:
            print("Invalid input. Please enter a valid number.")
            return
        else:
            print(f"You chose {userChoice}")
            print(rock_paper_scissors[userChoice])
        computerChoice = random.randint(0, 2)
        print(f"Computer chose {computerChoice}")
        print(rock_paper_scissors[computerChoice])
        if userChoice == computerChoice:
            print("It's a draw.")
        elif userChoice == 0 and computerChoice == 2:
            print("You win.")
        elif userChoice == 1 and computerChoice == 0:
            print("You win.")
        elif userChoice == 2 and computerChoice == 1:
            print("You win.")
        else:
            print("You lose.")
    except ValueError:
        print("Invalid input. Please enter a valid number.")
        return

if __name__ == "__main__":
    main()