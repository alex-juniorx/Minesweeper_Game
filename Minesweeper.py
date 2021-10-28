# MINESWEEPER GAME INTRODUCTION:
print("__________________________________")
print(" ")
print("WELCOME TO THE MINESWEEPER GAME!")
print("__________________________________")
print(" ")

from random import randint

# Creating a null board game:
board = []
for i in range(9):
    board.append(["="]*9)

# Function used to print the actual game board (with numbered rows and columns):
def print_board(given_board):
    # Numbering the columns:
    print("   0  1  2  3  4  5  6  7  8")
    print("   _  _  _  _  _  _  _  _  _")
    # count used only to number the rows:
    count = 0
    for row in given_board:
        print(count, end=" |"),
        print ("  ".join(row))
        count += 1

print_board(board)

# Function to generate the random positions [row, column] to the bombs:
def random_position(board):
    return [randint(0, len(board)-1), randint(0, len(board)-1)]

# Generating the position of the ten bombs (ensuring non-duplicate values):
bombs_position = []
for i in range(10):
    temp_position = random_position(board)
    while temp_position in bombs_position:
        temp_position = random_position(board)
    bombs_position.append(temp_position)

print(bombs_position)

# Creating the solution board for reference (it will be hidden from the player):
solution = []
    #Placing a default value "=" in the initial positions:
for i in range(9):
    solution.append(["="]*9)
    #Placing "#" values inn bomb positions:
for bomb in bombs_position:
    solution[bomb[0]][bomb[1]] = "#"
    #Placing the number of neighboring bombs in all positions.
for row in range(9):
    for column in range(9):
        bomb_count = 0
        if solution[row][column] == "#":
            continue
        elif row > 0 and row < 8 and column > 0 and column < 8:
            bomb_count += solution[row-1][column-1:column+2].count("#")
            bomb_count += solution[row][column-1:column+2].count("#")
            bomb_count += solution[row+1][column-1:column+2].count("#")
            solution[row][column] = str(bomb_count)
        elif row == 0 and column == 0:
            bomb_count += solution[row][column:column+2].count("#")
            bomb_count += solution[row+1][column:column+2].count("#")
            solution[row][column] = str(bomb_count)
        elif row == 0 and column == 8:
            bomb_count += solution[row][column-1:column+1].count("#")
            bomb_count += solution[row+1][column-1:column+1].count("#")
            solution[row][column] = str(bomb_count)
        elif row == 8 and column == 8:
            bomb_count += solution[row-1][column-1:column+1].count("#")
            bomb_count += solution[row][column-1:column+1].count("#")
            solution[row][column] = str(bomb_count)
        elif row == 8 and column == 0:
            bomb_count += solution[row-1][column:column+2].count("#")
            bomb_count += solution[row][column:column+2].count("#")
            solution[row][column] = str(bomb_count)
        elif row == 0 and column != 0 and column != 8:
            bomb_count += solution[row][column-1:column+2].count("#")
            bomb_count += solution[row+1][column-1:column+2].count("#")
            solution[row][column] = str(bomb_count)
        elif row == 8 and column != 0 and column != 8:
            bomb_count += solution[row-1][column-1:column+2].count("#")
            bomb_count += solution[row][column-1:column+2].count("#")
            solution[row][column] = str(bomb_count)
        elif column == 0 and row != 0 and row != 8:
            bomb_count += solution[row-1][column:column+2].count("#")
            bomb_count += solution[row][column:column+2].count("#")
            bomb_count += solution[row+1][column:column+2].count("#")
            solution[row][column] = str(bomb_count)
        elif column == 8 and row != 0 and row != 8:
            bomb_count += solution[row-1][column-1:column+1].count("#")
            bomb_count += solution[row][column-1:column+1].count("#")
            bomb_count += solution[row+1][column-1:column+1].count("#")
            solution[row][column] = str(bomb_count)
        
print_board(solution)


# Starting the game and initiating an interactive loop:
    #Obs.: A initial invalid input is given, only to start the loop.
selected_r, selected_c = 9, 9
while[selected_r, selected_c] not in bombs_position:
    print(".............................")

    #Asking for the user's input and avoiding a bad entry error:
    try:
        selected_r, selected_c = input("Go ahead buddy, select a valid \"row/column\" value: ").split("/")
        selected_r = int(selected_r)
        selected_c = int(selected_c)
    except:
        print(" ")
        print("Are you sure this is a valid \"row/column\" value?")
        continue
    
    #In case the selected location is out of the board:
    if (selected_r > 8 or selected_r < 0) or (selected_c > 8 or selected_c < 0):
        print(" ")
        print("Hey, both row and column values should be from 0 (zero) to 8 (eight). You knew that, right?!")

    #In case the same location is chosen again:
    elif board[selected_r][selected_c] != "=":
        print(" ")
        print("Hm, sorry! It looks like you have already selected this one.")
    
    #In case a bomb position is selected:
    elif [selected_r, selected_c] in bombs_position:
        board[selected_r][selected_c] = "#"
        print(" ")
        print_board(board)
        print(" ")
        print("Ouch, you stepted on a bomb! Game Over! :(")
        break      
    
    #In case the selected location is safe (without a bomb):
    elif solution[selected_r][selected_c] != "#":
        board[selected_r][selected_c] = solution[selected_r][selected_c]
        print("")
        print_board(board)


    







