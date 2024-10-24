#!E:\GIT\Python\Datacamp\Intermediate_Python_Dictionary\venv\Scripts\python.exe

# Create a plot with x and y data
europe = {'spain':'madrid', 'france':'paris', 'germany':'bonn',
          'norway':'oslo', 'italy':'rome', 'poland':'warsaw',
          'australia':'vienna' }

# Update capital of germany
europe['germany'] = 'berlin'

# Remove australia
del europe['australia']

# Print europe
print(europe)
