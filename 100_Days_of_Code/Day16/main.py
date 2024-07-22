import turtle
import prettytable

def main():
    # Your code here
    print("Hello World")
    timmy = turtle.Turtle() # Create a turtle object
    print(timmy)
    
    myScreen = turtle.Screen() # Create a screen object to display the turtle
    myScreen.canvheight = 400
    myScreen.canvwidth = 400
    myScreen.bgcolor("white")
    myScreen.title("Turtle Graphics")
    myScreen.setup(400, 400)
    
    timmy.shape("turtle") # Change the shape of the turtle
    timmy.color("red") # Change the color of the turtle
    timmy.forward(100) # Move the turtle forward by 100 units
    timmy.right(90) # Turn the turtle right by 90 degrees
    timmy.forward(100)
    timmy.right(90)
    timmy.forward(100)
    timmy.right(90)
    timmy.forward(100)
    
    mytable = prettytable.prettytable()
    print(mytable)
    myScreen.exitonclick() # Close the screen when clicked
    

if __name__ == "__main__":
    main()