travelLog = [
  {
    "country": "France",
    "visits": 12,
    "cities": ["Paris", "Lille", "Dijon"]
  },
  {
    "country": "Germany",
    "visits": 5,
    "cities": ["Berlin", "Hamburg", "Stuttgart"]
  },
]

def AddNewLog(logList, country, visits, cities):
    newLog = None
    if((type(logList) == list) and 
       (type(country) == str) and
       (type(cities) == str or type(cities) == list) and
       (type(visits) == int)):
        newLog = {
            "country": country,
            "visits": visits,
            "cities": cities
        }
        logList.append(newLog)
    return newLog

def main():
    # Your code here
    country = input("What is the country you visited?: ")
    visits = int(input("How many times have you visited the country?: "))
    cities = input("What are the cities you visited in the country? (comma separated): ")
    cities = cities.split(",")
    print(cities)
    
    try:
        visits = int(visits)
        AddNewLog(travelLog, country, visits, cities)
        print(f"I've been to {travelLog[2]['country']} {travelLog[2]['visits']} times.")
        print(f"My favourite city was {travelLog[2]['cities'][0]}.")
    except:
        print("Invalid input, please enter a valid input")
        

if __name__ == "__main__":
    main()