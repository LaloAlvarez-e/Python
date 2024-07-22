def main():
    
    fruits = ["Strawberries", "Nectarines", "Apples", "Grapes", "Peaches", "Cherries", "Pears"]
    vegetables = ["Spinach", "Kale", "Tomatoes", "Celery", "Potatoes"]
    
    dirtyDozen = [ fruits, vegetables ]
    #ill a list with states of america
    stateOfAmerica = ["Alabama", "Alaska", "Arizona", "Arkansas", 
                      "California", "Colorado", "Connecticut", 
                      "Delaware", "Florida", "Georgia", "Hawaii", 
                      "Idaho", "Illinois", "Indiana", "Iowa", 
                      "Kansas", "Kentucky", "Louisiana", "Maine", 
                      "Maryland", "Massachusetts", "Michigan", 
                      "Minnesota", "Mississippi", "Missouri", "Montana", 
                      "Nebraska", "Nevada", "New Hampshire", "New Jersey", 
                      "New Mexico", "New York", "North Carolina", 
                      "North Dakota", "Ohio", "Oklahoma", "Oregon", 
                      "Pennsylvania", "Rhode Island", "South Carolina", 
                      "South Dakota", "Tennessee", "Texas", "Utah", 
                      "Vermont", "Virginia", "Washington", "West Virginia", 
                      "Wisconsin", "Wyoming"]
    sortedStateOfAmerica = sorted(stateOfAmerica)
    numberOfStates = len(sortedStateOfAmerica)
    print(f"Number of states: {numberOfStates}\n{sortedStateOfAmerica}\n")

if __name__ == "__main__":
    main()