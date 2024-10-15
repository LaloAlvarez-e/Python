import turtlegraphics

class Snake:
    def __init__(self, screenSize=(600,600) , initial_length=3, startPos=[0, 0], stepSize=20, foodObject=None):
        self.width = screenSize[0]
        self.heigth = screenSize[1]
        self.startPos = startPos
        self.increasePos = [stepSize, 0]  
        self.snake = []
        self.createBody(initial_length, startPos)
        self.foodObject = foodObject
            
    def createBody(self, length=3, startPos=[0, 0]):
        for body in range(0, length):
            bodyMap = {}
            bodyMap['index'] = body
            bodyMap['object'] = turtlegraphics.TurtleGraphics(1, "white")
            bodyMap['object'].SetSpeed(0)
            bodyMap['currentPos'] = [(startPos[0]-(self.increasePos[0]*body)), (self.increasePos[1] * startPos[1])]
            bodyMap['object'].SetPosition(bodyMap['currentPos'][0], bodyMap['currentPos'][1])
            if(body != 0):
                bodyMap['nextPos'] = self.snake[body-1]['currentPos']
            else:
                bodyMap['nextPos'] = self.increasePos
            self.snake.append(bodyMap)
            print(self.snake)
            print(self.snake[body])

    def move(self):
        
        foodCoord = self.foodObject.getCoordenates() if self.foodObject != None else [self.width + 1, self.heigth + 1]
        print(f"Food coordinates: {foodCoord}")
        for body in range(0, len(self.snake)):
            self.snake[body]['object'].SetPosition(self.snake[body]['nextPos'][0], self.snake[body]['nextPos'][1])
            self.snake[body]['currentPos'] = self.snake[body]['object'].GetCoordinates()
            if(body == 0):
                newPosition = [self.snake[body]['currentPos'][0]+self.increasePos[0], self.snake[body]['currentPos'][1]+self.increasePos[1]]
            else:
                newPosition =  self.snake[body-1]['currentPos']  
            
            print(f"newPosition: {newPosition}")
            if(((foodCoord[0] >  self.snake[body]['currentPos'][0]) and (foodCoord[0] <  newPosition[0]))  and 
               ((foodCoord[1] >  self.snake[body]['currentPos'][1]) and (foodCoord[1] <  newPosition[1]))):
                self.snake.append({'index': len(self.snake), 'object': turtlegraphics.TurtleGraphics(1, "white")})
                self.snake[len(self.snake)-1]['object'].SetSpeed(0)
                self.snake[len(self.snake)-1]['currentPos'] = self.snake[len(self.snake)-2]['currentPos']
                self.snake[len(self.snake)-1]['object'].SetPosition(self.snake[len(self.snake)-1]['currentPos'][0], self.snake[len(self.snake)-1]['currentPos'][1])
                self.snake[len(self.snake)-1]['nextPos'] = self.snake[len(self.snake)-2]['nextPos']
                self.foodObject.refresh()
            self.snake[body][ 'nextPos'] =newPosition
    
    def SetDirection(self, direction):
        if(direction == "Rigth"):
            self.increasePos = [20, 0]
        elif(direction == "Left"):
            self.increasePos = [-20, 0]
        elif(direction == "Up"):
            self.increasePos = [0, 20]
        elif(direction == "Down"):
            self.increasePos = [0, -20]
        else:
            self.increasePos = [20, 0]
            
    def GetDirection(self):
        if(self.increasePos[0] == 20 and self.increasePos[1] == 0):
            return "Rigth"
        elif(self.increasePos[0] == -20 and self.increasePos[1] == 0):
            return "Left"
        elif(self.increasePos[0] == 0 and self.increasePos[1] == 20):
            return "Up"
        elif(self.increasePos[0] == 0 and self.increasePos[1] == -20):
            return "Down"
        else:
            return "Rigth"
        
            
