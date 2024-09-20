#!E:\GIT\Python\100_Days_of_Code\Day20\venv\Scripts\python.exe
import turtlegraphics
import snake

width = 600
heigth = 600

stepSize = 20
initialCoord = [0, 0]

running = True

snakeObject = snake.Snake((width,heigth), 3, initialCoord, stepSize)
myScreen = turtlegraphics.TurtleScreen((width,heigth), "black", "Snake")



def EventRigth():
    print("Rigth")
    if(snakeObject.GetDirection() != "Left"):
        snakeObject.SetDirection("Rigth")

def EventLeft():
    print("Left")
    if(snakeObject.GetDirection() != "Rigth"):
        snakeObject.SetDirection("Left")

def EventUp():
    print("Up")
    if(snakeObject.GetDirection() != "Down"):
        snakeObject.SetDirection("Up")  

def EventDown():
    print("Down")
    if(snakeObject.GetDirection() != "Up"):
        snakeObject.SetDirection("Down")    
    
def EventExit():   
    print("Exit")
    global running
    running = False
    
    
def main():    
    print("Welcome to Snake Game")
    myScreen.ListenOnKey(EventRigth, "Right")
    myScreen.ListenOnKey(EventLeft, "Left")
    myScreen.ListenOnKey(EventUp, "Up")
    myScreen.ListenOnKey(EventDown, "Down")
    myScreen.ListenOnKey(EventExit, "Control_L")
    myScreen.StartListen()
    while (True == running):
        myScreen.UpdateScreen(0.05)
        snakeObject.move()
        
    myScreen.ExitOnClick()
    
if __name__ == "__main__":
    main()