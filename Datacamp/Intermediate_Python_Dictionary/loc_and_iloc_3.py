#!E:\GIT\Python\Datacamp\Intermediate_Python_Dictionary\venv\Scripts\python.exe

# Import pandas as pd
import pandas as pd

# Import the cars.csv data: cars
cars = pd.read_csv("E:\\GIT\\Python\\Datacamp\\Intermediate_Python_Dictionary\\cars.csv", index_col=0)

print(cars)

# Print out drives_right column as Series
drives_right_series = cars.loc[:, "drives_right"]
print(drives_right_series)

# Print out drives_right column as DataFrame
drives_right_pd = cars.loc[:, ["drives_right"]]
print(drives_right_pd)



# Print out cars_per_cap and drives_right as DataFrame
both_pd = cars.loc[:, ["cars_per_cap", "drives_right"]]
print(both_pd)
