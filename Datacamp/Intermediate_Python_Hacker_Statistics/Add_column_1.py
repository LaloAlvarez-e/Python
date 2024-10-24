#!E:\GIT\Python\Datacamp\Intermediate_Python_Hacker_Statistics\venv\Scripts\python.exe

# Import pandas as pd
import pandas as pd
cars = pd.read_csv('E:\\GIT\\Python\\Datacamp\\Intermediate_Python_Hacker_Statistics\\cars.csv', index_col = 0)

# Code for loop that adds COUNTRY column
cars["COUNTRY"] = cars["country"].apply(str.upper)



# Print cars
print(cars)