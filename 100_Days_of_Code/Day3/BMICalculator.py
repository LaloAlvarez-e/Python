def main():
    #get user input
    height = input("enter your height in m: ")
    weight = input("enter your weight in kg: ")
    #calculate the BMI
    try:
        height = float(height) 
        weight = float(weight)
        bmi = weight / (height ** 2)
        
        stringAdd = None
        if bmi < 18.5:
            stringAdd = "you are underweight."
        elif bmi < 25:
            stringAdd = "you have a normal weight."
        elif bmi < 30:
            stringAdd = "you are slightly overweight."
        elif bmi < 35:
            stringAdd = "you are obese."
        else:
            stringAdd = "you are clinically obese."
        bmiDescription = f"Your BMI is {str(bmi)}, {stringAdd}"
        print(bmiDescription)
    except ValueError:
        print("Invalid input. Please enter a valid number.")
        return

if __name__ == "__main__":
    main()