#!E:\GIT\Python\Datacamp\Intermediate_Python_Logic_Control_Filtering\venv\Scripts\python.exe

# Import cars data
import pandas as pd
import numpy as np
cars = pd.read_csv('E:\\GIT\\Python\\Datacamp\\Intermediate_Python_Logic_Control_Filtering\\cars.csv', index_col = 0)

# Create medium: observations with cars_per_cap between 100 and 500
cpc = cars['cars_per_cap']
between = np.logical_and(cpc > 100, cpc < 500)
medium = cars[between]

# Print medium
print(medium)