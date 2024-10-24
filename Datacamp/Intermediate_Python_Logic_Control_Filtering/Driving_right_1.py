#!E:\GIT\Python\Datacamp\Intermediate_Python_Logic_Control_Filtering\venv\Scripts\python.exe

# Import cars data
import pandas as pd
cars = pd.read_csv('E:\\GIT\\Python\\Datacamp\\Intermediate_Python_Logic_Control_Filtering\\cars.csv', index_col = 0)


# Extract drives_right column as Series: dr
dr = cars['drives_right']
print(dr)

# Use dr to subset cars: sel
sel = cars[dr]

# Print sel
print(sel)