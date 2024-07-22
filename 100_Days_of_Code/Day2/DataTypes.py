def main():
    two_digit_number = input()
    try:
        two_digit_number = two_digit_number[0:2]
        digitlen = len(two_digit_number)
        two_digit_number = int(two_digit_number)
        arrayOfValues = []
        sumOfValue = 0
        for i in range(0, digitlen):
            arrayOfValues.append(two_digit_number%10)
            sumOfValue += arrayOfValues[i]
            two_digit_number = int(two_digit_number/10)
        print(str(sumOfValue))
    except ValueError:
        print("Invalid input. Please enter a two digit number.")
        return

if __name__ == "__main__":
    main()