#!E:\GIT\Python\Datacamp\Intermediate_Python_Dictionary\venv\Scripts\python.exe

# Import pandas as pd
import pandas as pd

# Import the cars.csv data: cars
cars = pd.read_csv("E:\\GIT\\Python\\Datacamp\\Intermediate_Python_Dictionary\\cars.csv", index_col=0)

print(cars)

# Print out drives_right value of Morocco
morroco_row = cars.loc[["MOR"], ["drives_right"]]
print(morroco_row)

# Print sub-DataFrame
aus_egypt = cars.loc[["RU", "MOR"], ["country", "drives_right"]]
print(aus_egypt)


# Print out drives_right value of Morocco
morroco_row = cars.iloc[[5], [2]]
print(morroco_row)

# Print sub-DataFrame
aus_egypt = cars.iloc[[4, 5], [1, 2]]
print(aus_egypt)