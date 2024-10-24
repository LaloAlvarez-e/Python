#!E:\GIT\Python\Datacamp\Intermediate_Python_Dictionary\venv\Scripts\python.exe
# Dictionary of dictionaries
europe = { 'spain': { 'capital':'madrid', 'population':46.77 },
           'france': { 'capital':'paris', 'population':66.03 },
           'germany': { 'capital':'berlin', 'population':80.62 },
           'norway': { 'capital':'oslo', 'population':5.084 } }

# Print out the capital of France
cap_france = europe['france']['capital']
print(cap_france)

# Create sub-dictionary data
data = {}
data["capital"] = "rome"
data["population"] = 59.83

# Add data to europe under key 'italy'
europe["italy"] = data 

# Print europe
print(europe)
