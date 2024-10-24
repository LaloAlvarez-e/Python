#!E:\GIT\Python\Datacamp\Intermediate_Python_Dictionary\venv\Scripts\python.exe

# Import pandas as pd
import pandas as pd

# Import the cars.csv data: cars
cars = pd.read_csv("E:\\GIT\\Python\\Datacamp\\Intermediate_Python_Dictionary\\cars.csv", index_col=0)


# Print out country column as Pandas Series
countty_col = cars['country']
print(countty_col)

# Print out country column as Pandas DataFrame
country_col_pd = cars[['country']]
print(country_col_pd)

# Print out DataFrame with country and drives_right columns
country_dr = cars[['country', 'drives_right']]
print(country_dr)
