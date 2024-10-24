#!E:\GIT\Python\Datacamp\Intermediate_Python_Loops\venv\Scripts\python.exe

# Definition of dictionary
europe = {'spain':'madrid', 'france':'paris', 'germany':'berlin',
          'norway':'oslo', 'italy':'rome', 'poland':'warsaw', 'austria':'vienna' }
          
# Iterate over europe
for country in europe.items():
    print("the capital of " + country[0] + " is " + country[1])