#!E:\GIT\Python\Datacamp\Intermediate_Python_Loops\venv\Scripts\python.exe

# areas list
areas = [11.25, 18.0, 20.0, 10.75, 9.50]

# Change for loop to use enumerate() and update print()
for index, area in enumerate(areas,1) :
    print("room " + str(index) + ": " + str(area))