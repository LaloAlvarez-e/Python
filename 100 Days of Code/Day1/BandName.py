

def main():
    print("Welcome to the Band Name Generator.")
    myCity = input("What's the name of the city you grew up in?\n")
    myPetName = input("What's your pet's name?\n")
    myBandName = myCity + " " + myPetName   
    
    print ("Your band name could be " + myBandName)

if __name__ == "__main__":
    main()
    print("Hello, world!")