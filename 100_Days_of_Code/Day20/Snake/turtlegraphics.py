import turtle
import random
import time

class TurtleScreen:
    def __init__(self, size, color, title):
        self.myScreen = turtle.Screen()
        self.myScreen.colormode(255)
        self.myScreen.setup(size[0], size[1])
        self.myScreen.bgcolor(color)
        self.myScreen.title(title)
        self.myScreen.tracer(0)
        
    def ExitOnClick(self):
        self.myScreen.exitonclick()
    
    def StartListen(self, size=None):
        if(size != None):
            self.myScreen.listen(size[0], size[1])
        else:
            self.myScreen.listen()  
        
    def ListenOnKey(self, function, key):
        self.myScreen.onkey(function, key)
        
    def ClearScreen(self):
        self.myScreen.clear()
    
    def UpdateScreen(self, delay=None):
        self.myScreen.update()
        if(delay != None):
            time.sleep(delay)

class TurtleGraphics:
    def __init__(self, size, color):
        self.myHandler = turtle.Turtle() # Create a turtle object
        self.myHandler.shape("square") # Change the shape of the turtle
        self.myHandler.pensize(size)
        self.myHandler.color(color) # Change the color of the turtle
        
    
    def Color(self, color):
        self.myHandler.color(color)
        
    def SetAngle(self, angle, color=None):
        if(color != None):
            self.myHandler.color(color)
        self.myHandler.setheading(angle)
    
    def AddAngle(self, angle, color=None):
        if(color != None):
            self.myHandler.color(color)
        myCurrentAngle = self.myHandler.heading()
        myCurrentAngle += angle
        self.myHandler.setheading(myCurrentAngle)
        
    def Forward(self, distance, color=None):
        if(color != None):
            self.myHandler.color(color)
        self.myHandler.forward(distance)
        
    def ForwardBlank(self, distance, color=None):
        if(color != None):
            self.myHandler.color(color)
        self.myHandler.penup()
        self.myHandler.forward(distance)
        self.myHandler.pendown()
        
    def Backward(self, distance, color=None):
        if(color != None):
            self.myHandler.color(color)
        self.myHandler.backward(distance)
    
    def Move(self, direction, angle, distance, color=None):
        myDirection = [self.myHandler.right, self.myHandler.left, self.myHandler.setheading]
        if(color != None):
            self.myHandler.color(color)
        myDirection[direction](angle)
        self.myHandler.backward(distance)
        
    def MoveBackward(self, direction, angle, distance, color=None):
        myDirection = [self.myHandler.right, self.myHandler.left, self.myHandler.setheading]
        if(color != None):
            self.myHandler.color(color)
        myDirection[direction](angle)
        self.myHandler.backward(distance)
        
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
    
        
    def SetSpeed(self, speed):
        speedValue = ["fastest", "fast", "normal", "slow", "slowest"]
        self.myHandler.speed(speedValue[speed])
        
    def SetPosition(self, x, y):
        self.myHandler.penup()
        self.myHandler.setpos(x, y)
        self.myHandler.pendown()
        
    def SetPenSize(self, size):
        self.myHandler.pensize(size)
        
    def GetRandomColor():
        red = random.randint(0, 255)
        green = random.randint(0, 255)
        blue = random.randint(0, 255)
        return (red, green, blue)
    
    def Clear(self):
        self.myHandler.clear()