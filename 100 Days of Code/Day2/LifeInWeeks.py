maxAge = 90
daysPerYear = 365
weeksPerYear = 52
monthsPerYear = 12

def main():
    age = input("What is your current age?\n")
    try:
        age = int(age)
        yearsRemaining = maxAge - age
        daysRemaining = yearsRemaining * daysPerYear
        weeksRemaining = yearsRemaining * weeksPerYear
        monthsRemaining = yearsRemaining * monthsPerYear
        print(f"You have {daysRemaining} days, {weeksRemaining} weeks, and {monthsRemaining} months left.")
    except ValueError:
        print("Invalid input. Please enter a valid number.")    
        return

if __name__ == "__main__":
    main()