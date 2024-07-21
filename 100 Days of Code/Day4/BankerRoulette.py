import random

coworker = ["Angela", "Ben", "Jenny", "Michael", "Chloe"]

def main():
    # Add your code here
    numberOfCoworkers = len(coworker)
    index = random.randint(0, numberOfCoworkers - 1)
    print(f"{coworker[index]} is going to buy the meal today!")

if __name__ == "__main__":
    main()