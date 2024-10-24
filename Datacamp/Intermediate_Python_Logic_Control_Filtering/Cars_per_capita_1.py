#!E:\GIT\Python\Datacamp\Intermediate_Python_Logic_Control_Filtering\venv\Scripts\python.exe

# Import cars data
import pandas as pd
cars = pd.read_csv('E:\\GIT\\Python\\Datacamp\\Intermediate_Python_Logic_Control_Filtering\\cars.csv', index_col = 0)

# Convert code to a one-liner
cpc = cars['cars_per_cap']
many_cars = cpc > 500
car_maniac = cars[many_cars]

# Print car_maniac
print(car_maniac)