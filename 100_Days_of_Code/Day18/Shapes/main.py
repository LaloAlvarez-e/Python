#!E:\GIT\Python\100_Days_of_Code\Day18\venv\Scripts\python.exe

import turtle

class TurtleGraphics:
    def __init__(self, size, color):
        self.myHandler = turtle.Turtle() # Create a turtle object
        self.myHandler.shape("turtle") # Change the shape of the turtle
        self.myHandler.color(color) # Change the color of the turtle
        self.myScreen = turtle.Screen()
        self.myScreen.setup(size[0], size[1])
        self.myScreen.bgcolor("white")
        self.myScreen.title("Turle Graphics")
    
    def Color(self, color):
        self.myHandler.color(color)
    
    def Move(self, direction, angle, distance):
        myDirection = [self.myHandler.right, self.myHandler.left]
        myDirection[direction](angle)
        self.myHandler.forward(distance)
        
    def MoveDash(self, direction, angle, distance):
        myDirection = [self.myHandler.right, self.myHandler.left]
        myFunctions = [self.myHandler.pendown, self.myHandler.penup]
        myDirection[direction](angle)
        ranges = int(distance/10)
        for i in range(ranges):
            myFunctions[i%2]()
            toMove = distance if distance < 10 else 10
            self.myHandler.forward(toMove)
            distance = distance - 10
        self.myHandler.pendown()
    
    def MoveRight(self, angle, distance):
        self.Move(0, angle, distance)
        
    def MoveLeft(self, angle, distance):
        self.Move(1, angle, distance)
        
    def MoveRightDash(self, angle, distance):
        self.MoveDash(0, angle, distance)        
        
    def MoveLeftDash(self, angle, distance):
        self.MoveDash(1, angle, distance)
        
    def Shapes(self, sides, size):
        for i in range(sides):
            self.myHandler.forward(size)
            self.myHandler.right(360/sides)
def main():
    # Your code here
    print("Hello World")
    myHandler = TurtleGraphics((400, 400), "aqua")
    myShapes = 9
    myColors = ["red", "blue", "green", "black", "brown", "yellow", "orange", "purple", "pink"] 
    
    i = 3
    for shape in range(myShapes):
        myHandler.Color(myColors[shape])
        myHandler.Shapes(i, 100)
        i += 1
    

if __name__ == "__main__":
    main()