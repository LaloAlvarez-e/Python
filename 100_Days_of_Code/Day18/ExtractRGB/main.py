#!E:\GIT\Python\100_Days_of_Code\Day18\venv\Scripts\python.exe

import colorgram 

import turtle
import random

class TurtleGraphics:
    def __init__(self, size, color):
        self.myHandler = turtle.Turtle() # Create a turtle object
        self.myScreen = turtle.Screen()
        self.myScreen.colormode(255)
        #self.myHandler.shape("turtle") # Change the shape of the turtle
        self.myHandler.pensize(1)
        self.myHandler.color(color) # Change the color of the turtle
        self.myScreen.setup(size[0], size[1])
        self.myScreen.bgcolor("white")
        self.myScreen.title("Turle Graphics")
        
    
    def Color(self, color):
        self.myHandler.color(color)
    
    def Move(self, direction, angle, distance, color=None):
        myDirection = [self.myHandler.right, self.myHandler.left, self.myHandler.setheading]
        if(color != None):
            self.myHandler.color(color)
        myDirection[direction](angle)
        self.myHandler.forward(distance)
        
    def MoveDash(self, direction, angle, distance, color=None):
        myDirection = [self.myHandler.right, self.myHandler.left, self.myHandler.setheading]
        myFunctions = [self.myHandler.pendown, self.myHandler.penup]
        if(color != None):
            self.myHandler.color(color)
        myDirection[direction](angle)
        ranges = int(distance/10)
        for i in range(ranges):
            myFunctions[i%2]()
            toMove = distance if distance < 10 else 10
            self.myHandler.forward(toMove)
            distance = distance - 10
        self.myHandler.pendown()
    
    def MoveRightAngle(self, angle, distance, color=None):
        self.Move(0, angle, distance, color)
        
    def MoveLeftAngle(self, angle, distance, color=None):
        self.Move(1, angle, distance, color)
        
    def MoveUp(self, distance, color=None):
        self.Move(2, 90, distance, color)
        
    def MoveDown(self, distance, color=None):
        self.Move(2, 270, distance, color)
        
    def MoveRight(self, distance, color=None):
        self.Move(2, 0, distance, color)
        
    def MoveLeft(self, distance, color=None):
        self.Move(2, 180, distance, color)
        
    def MoveRightAngleDash(self, angle, distance, color=None):
        self.MoveDash(0, angle, distance, color)        
        
    def MoveLeftAngleDash(self, angle, distance, color=None):
        self.MoveDash(1, angle, distance, color)
        
    def MoveRightDash(self, distance, color=None):
        self.MoveDash(2, 0, distance, color)        
        
    def MoveLeftDash(self, distance, color=None):
        self.MoveDash(2, 180, distance, color)
        
    def MoveUpDash(self, distance, color=None):
        self.MoveDash(2, 90, distance, color)        
        
    def MoveDownDash(self, distance, color=None):
        self.MoveDash(2, 270, distance, color)
        
    def Shapes(self, sides, size):
        for i in range(sides):
            self.myHandler.forward(size)
            self.myHandler.right(360/sides)
            
    def Circle(self, radius, angle=None, color=None):
        if(color != None):
            self.myHandler.color(color)
        if(angle != None):
            self.myHandler.setheading(angle)
        self.myHandler.circle(radius)

    def Spirograph(self, size, angle):
        for i in range(360//angle):
            self.myHandler.color(self.GetRandomColor())
            self.myHandler.circle(size)
            self.myHandler.right(angle)
            
    def Dot(self, size, move=None, color=None):
        self.myHandler.penup()
        if(color != None):
            self.myHandler.dot(size, color)
        else:
            self.myHandler.dot(size)
        if(None != move):
            self.myHandler.forward(move)
        self.myHandler.pendown()
        
    def GetCoordinates(self):
        return self.myHandler.pos()
    
    def ExitOnClick(self):
        self.myScreen.exitonclick()
        
    def SetSpeed(self, speed):
        speedValue = ["fastest", "fast", "normal", "slow", "slowest"]
        self.myHandler.speed(speedValue[speed])
        
    def SetPosition(self, x, y):
        self.myHandler.penup()
        self.myHandler.setpos(x, y)
        self.myHandler.pendown()
        
    def GetRandomColor():
        red = random.randint(0, 255)
        green = random.randint(0, 255)
        blue = random.randint(0, 255)
        return (red, green, blue)

def main():
    # Your code here
    print("Hello World")
    myImage = "E:\\GIT\\Python\\100_Days_of_Code\\Day18\\ExtractRGB\\picto.jpeg"
    myColors = colorgram.extract(myImage, 255)
    myColorList = []
    for color in myColors:
        red = color.rgb.r
        green = color.rgb.g
        blue = color.rgb.b
        newColor = (red, green, blue)
        myColorList.append(newColor)
    
    print(myColorList)
    
    myWidth = 200
    myHeight = 200
    dotsPerRow = 10
    numberOfRows = 10
    initialX = -(myWidth/2)
    initialY = -(myHeight/2)
    size = myWidth/dotsPerRow
    offset = myHeight/numberOfRows
    myHandler = TurtleGraphics((myWidth, myHeight), (0,0,0))
    myHandler.SetSpeed(0)
    
    for rowNum in range(numberOfRows):
        myHandler.SetPosition(initialX, initialY)
        for columnNum in range(dotsPerRow):
            myHandler.Dot(10, size, random.choice(myColorList))
        initialY = initialY + offset
    
    myHandler.ExitOnClick()
    

if __name__ == "__main__":
    main()