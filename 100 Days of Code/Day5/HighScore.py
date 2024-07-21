def main():
    # Your code here
    studentRecord = input("Input a list of student scores separate by space: ")
    studentRecord = studentRecord.split(" ")
    highestScore = 0.0
    for score in studentRecord:
        storeFloat = None
        try:
            storeFloat = float(score)
        except ValueError:
            print(f"Invalid input. Please enter a valid score. {score} is not a valid score.")
        if storeFloat != None:
            if storeFloat > highestScore:
                highestScore = storeFloat
    print(f"The highest score in the class is: {highestScore}")

    
if __name__ == "__main__":
    main()