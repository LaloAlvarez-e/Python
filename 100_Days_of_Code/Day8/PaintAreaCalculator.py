def PaintCalculator(wallHeight, wallWidth, coverageM2):
    if((type(wallHeight) != float and type(wallHeight) != int)or 
       (type(wallWidth)  != float and type(wallWidth)  != int) or
       (type(coverageM2) != float and type(coverageM2) != int)):
        print("Invalid input. Please enter a valid number.")
        return
    area = wallHeight * wallWidth
    numberOfCans = area / coverageM2
    if numberOfCans % 1 != 0:
        numberOfCans += 1
    numberOfCans = int(numberOfCans)
    return numberOfCans

def main():
    # Your code here
    wallHeight = input("Height of wall: ")
    wallWidth = input("Width of wall: ")   
    coverageM2 = 5
    try:
        wallHeight = float(wallHeight)
        wallWidth = float(wallWidth)
    
        numberOfCans = PaintCalculator(wallHeight, wallWidth, coverageM2)
        print(f"You'll need {numberOfCans} cans of paint.")
    except ValueError:
        print("Invalid input. Please enter a valid number.")
        return

if __name__ == "__main__":
    main()