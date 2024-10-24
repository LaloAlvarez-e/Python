#!E:\GIT\Python\Datacamp\Intermediate_Python_Dictionary\venv\Scripts\python.exe

# Import pandas as pd
import pandas as pd

# Import the cars.csv data: cars
cars = pd.read_csv("E:\\GIT\\Python\\Datacamp\\Intermediate_Python_Dictionary\\cars.csv", index_col=0)

print(cars)

# Print out observation for Japan
japan_row = cars.loc["JPN"]
print(japan_row)

# Print out observations for Australia and Egypt
aus_egypt = cars.loc[["AUS", "EG"]]
print(aus_egypt)




# Print out observation for Japan
japan_row = cars.iloc[2]
print(japan_row)

# Print out observations for Australia and Egypt
aus_egypt = cars.iloc[[1, 6]]
print(aus_egypt)