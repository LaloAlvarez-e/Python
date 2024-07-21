def main():
    # Your code here
    studentHeights = input("Input a list of student scores separate by space: ")
    studentHeights = studentHeights.split(" ")
    heightSum = 0.0
    numberOfStudents = 0
    for score in studentHeights:
        storeFloat = None
        try:
            storeFloat = float(score)
        except ValueError:
            print(f"Invalid input. Please enter a valid score. {score} is not a valid score.")
        if storeFloat != None:
            numberOfStudents += 1
            heightSum += storeFloat
    if(numberOfStudents > 0):
        averageHeight = int(round(heightSum / numberOfStudents))
        print(f"total height = {int(heightSum)}")
        print(F"number of students = {numberOfStudents}")
        print(f"average height = {averageHeight}")

    
if __name__ == "__main__":
    main()