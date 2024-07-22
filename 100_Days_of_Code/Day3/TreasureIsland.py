def printFrog():
    #create a tresuare frog with ascci art
    print('''
    ***************************************************************
                                .-----.
                                /7  .  (
                            /   .-.  //
                            /   /   /  //
                            / `  )   (   )
                            / `   )   ).  //
                        .'  _.   /_/  . |
        .--.           .' _.' )`.        |
        (    `---...._.'   `---.'_)    ..  //
        /            `----....___    `. /  |
        `.           _ ----- _   `._  )/  |
            `.       /"  /   /"  /`.  `._   |
            `.    ((O)` ) ((O)` ) `.   `._//
                `-- '`---'   `---' )  `.    `-.
                /                  ` /      `-.
                .'                      `.       `.
                /                     `  ` `.       `-.
        .--.   / ===._____.======. `    `   `. .___.--`     .''.
        ' .` `-. `.                )`. `   ` ` /          .' . '  8)
    (8  .  ` `-.`.               ( .  ` `  .`/      .'  '    ' /
        /  `. `    `-.               ) ` .   ` ` /  .'   ' .  '  /
        / ` `.  ` . /`.    .--.     |  ` ) `   .``/   '  // .  /
        `.  ``. .   / /   .-- `.  (  ` /_   ` . / ' .  '/   .'
            `. ` /  `  / /  '-.   `-'  .'  `-.  `   .  .'/  .'
            / `.`.  ` / /    ) /`._.`       `.  ` .  .'  /
        LGB    |  `.`. . / /  (.'               `.   .'  .'
            __/  .. / / ` ) /                     /.' .. /__
    .-._.-'     '"  ) .-'   `.                   (  '"     `-._.--.
    (_________.-====' / .' /_)`--..__________..-- `====-. _________)
    *********************************************
    ''')
    

def getDirection():
    returnCode = 0
    direction = None
    if(0 == returnCode):
        direction = input("You're at a crossroad. Where do you want to go? Type 'left' or 'right' \n")
        direction = direction.lower()
        if(direction != "left" and direction != "right"):
            print("Invalid input. Please enter a valid direction.")
            returnCode = 1
        
    if(0 == returnCode):
        if direction == "right" :
            print("You fell into a hole. Game Over.")
            returnCode = 1
    return (returnCode)

def getAction():
    returnCode = 0
    action = None
    if(0 == returnCode):
        action = input("You've come to a lake. There is an island in the middle of the lake. Type 'wait' to wait for a boat. Type 'swim' to swim across.\n")
        action = action.lower()
        if action != "wait" and action != "swim":
            print("Invalid input. Please enter a valid action.")
            returnCode = 1
            
    if(0 == returnCode):
        if action == "swim":
            print("You were attacked by a trout. Game Over.")
            returnCode = 1
    return (returnCode)

def getDoor():
    returnCode = 0
    door = None
    if(0 == returnCode):
        door = input("You arrived at the island unharmed. There is a house with 3 doors. One red, one yellow, and one blue. Which color do you choose?\n")
        door = door.lower()
        if door != "red" and door != "yellow" and door != "blue":
            print("Invalid input. Please enter a valid door.")
            returnCode = 1
            
    if(0 == returnCode):
        if door == "red":
            print("You were burned by fire. Game Over.")
            returnCode = 1
        elif door == "blue":
            print("You were eaten by beasts. Game Over.")
            returnCode = 1
        elif door == "yellow":
            print("You found the treasure! You win!")
    return (returnCode)

def main():
    # Your code here
    returnCode = 0
    printFrog()
    print("Welcome to Treasure Island.\nYour mission is to find the treasure.")
    
    if(0 == returnCode): returnCode = getDirection()
    if(0 == returnCode): returnCode = getAction()
    if(0 == returnCode): returnCode = getDoor()


if __name__ == "__main__":
    main()