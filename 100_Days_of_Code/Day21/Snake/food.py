from turtle import Turtle
import random

class Food(Turtle):
    def __init__(self, screenSize=(600,600)):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_wid=0.5, stretch_len=0.5)
        self.color("blue")  
        self.speed("fastest")
        self.xPos = int((28/30)*screenSize[0])
        self.yPos = int((28/30)*screenSize[1])
        self.coordX = random.randint(-self.xPos, self.xPos)
        self.coordY = random.randint(-self.yPos, self.yPos)
        self.goto(self.coordX, self.coordY)
        
    def getCoordenates(self):
        return (self.coordX, self.coordY)
    
    def refresh(self):
        self.coordX = random.randint(-self.xPos, self.xPos)
        self.coordY = random.randint(-self.yPos, self.yPos)
        self.goto(self.coordX, self.coordY)
            
