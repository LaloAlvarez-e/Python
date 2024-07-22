def main():
    height = input()
    weight = input()
    try:
        height = float(height)
        weight = float(weight)
        bmi = weight / (height ** 2)
        bmi = int(bmi)
        print(str(bmi))
    except ValueError:
        print("Invalid input. Please enter a valid number.")
        return
    

if __name__ == "__main__":
    main()