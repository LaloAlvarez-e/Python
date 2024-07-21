def main():
    line1 = ["⬜️", "⬜️", "⬜️"]
    line2 = ["⬜️", "⬜️", "⬜️"]
    line3 = ["⬜️", "⬜️", "⬜️"]
    mapList = [line1, line2, line3]
    
    position = input("Where do you want to put the treasure? ex B3 \n")
    inputLen = None
    row = None
    column = None
    try:
        inputLen = len(position)
        if inputLen != 2:
            print(f"Invalid input. Please enter a valid position. {inputLen} is not valid")
            return
        
        maxRow = len(mapList)
        row = int(position[1])
        if((0 >= row) or (row > maxRow)):
            print(f"Invalid input. Please enter a valid position. Row should be between 1 and {maxRow}")
            return
        row -= 1
        
        maxColumn = len(mapList[0])
        column = position[0].upper()
        column = int(ord(column)) - int(ord("A"))
        if((0 > column) or (column > (maxColumn - 1))):
            print(f"Invalid input. Please enter a valid position. Column should be between A and {chr(65 + maxColumn - 1)}")
            return
        mapList[row][column] = "X"
        print(f"{line1}\n{line2}\n{line3}")
    except ValueError:
        print(f"Invalid input. Please enter a valid position. inputLen: {inputLen} row: {row} column: {column}")
        return
    
    

if __name__ == "__main__":
    main()