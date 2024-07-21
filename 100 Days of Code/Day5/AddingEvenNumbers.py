def main():
    # Your code here
    lastNumber = input("Enter the last number: ")
    try:
        lastNumberInt = int(lastNumber)
        if lastNumberInt < 2:
            return
        evenSum = 0
        for number in range(2, lastNumberInt + 1, 2):
            evenSum += number
        print(f"The sum of all even numbers from 2 to {lastNumberInt} is: {evenSum}")
    except ValueError:
        return

if __name__ == "__main__":
    main()