#!E:\GIT\Python\Datacamp\Basic_plots_with_Matplotlib\venv\Scripts\python.exe

import matplotlib.pyplot as plt

# Create a plot with x and y data
year = [1950, 1970, 1990, 2010]
pop = [2.519, 3.692, 5.263, 6.972]
plt.plot(year, pop)
plt.show()
plt.scatter(year, pop)
plt.show()
