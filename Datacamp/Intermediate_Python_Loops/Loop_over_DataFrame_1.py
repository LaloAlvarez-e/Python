#!E:\GIT\Python\Datacamp\Intermediate_Python_Loops\venv\Scripts\python.exe

# Import pandas as pd
import pandas as pd
cars = pd.read_csv('E:\\GIT\\Python\\Datacamp\\Intermediate_Python_Loops\\cars.csv', index_col = 0)


# Iterate over rows of cars
for lab, row in cars.iterrows():
    print(lab)
    print(row)