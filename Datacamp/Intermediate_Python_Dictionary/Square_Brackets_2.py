#!E:\GIT\Python\Datacamp\Intermediate_Python_Dictionary\venv\Scripts\python.exe

# Import pandas as pd
import pandas as pd

# Import the cars.csv data: cars
cars = pd.read_csv("E:\\GIT\\Python\\Datacamp\\Intermediate_Python_Dictionary\\cars.csv", index_col=0)

# Print out first 3 observations
first_rows = cars[0:3]
print(first_rows)

# Print out fourth, fifth and sixth observation
specific_rows = cars[3:6]
print(specific_rows)
