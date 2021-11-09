#MINESWEEPER GAME (9x9 Board, 15 Bombs)

#1 Creating a null board game:
board = []

for i in range(9):
    board.append(["[ ]"]*9)

#2 Function used to print the actual game board (with numbered rows and columns):
def print_board(given_board):
    # Numbering the columns:
    print("     0  1  2  3  4  5  6  7  8 ")
    print("   ----------------------------")
    # count used only to number the rows:
    count = 0
    for row in given_board:
        print(count, end=" | "),
        print ("".join(row))
        count += 1

#3 Generating the position of the ten bombs (ensuring non-duplicate values):
from random import randint

bombs_position = []

for i in range(15):
    temp_position = [randint(0, len(board)-1), randint(0, len(board)-1)]
    while temp_position in bombs_position:
        temp_position = [randint(0, len(board)-1), randint(0, len(board)-1)]
    bombs_position.append(temp_position)

#4 Creating the solution board for reference along the game (it will be hidden from the player):
solution = []

    #4.1 Placing a default value "[ ]" in the initial positions:
for i in range(9):
    solution.append(["[ ]"]*9)
    
    #4.2 Placing "[X]" values in the defined bomb positions:
for bomb in bombs_position:
    solution[bomb[0]][bomb[1]] = "[X]"
    
    #4.3 Placing the number of neighboring bombs in all positions, except for bomb positions.
for row in range(9):
    for column in range(9):
        bomb_count = 0
        if solution[row][column] == "[X]":
            continue
        else:
            for neighboring_row in range(row-1, row+2):
                for neighboring_column in range(column-1, column+2):
                    if neighboring_row == -1 or neighboring_row == 9 or neighboring_column == -1 or neighboring_column == 9:
                        continue
                    elif solution[neighboring_row][neighboring_column] == "[X]":
                        bomb_count += 1
            solution[row][column] = "[" + str(bomb_count) + "]"
print_board(solution) 

#5 Function created to reveal "[0]" locations, when a neighboring "[0]" is revealed by the player
def reveal_zeros():    
    #Obs.: While a new "[0]" is revealed, the loop should repeat
    repeat = True
    while repeat == True:
        repeat = False
        for row in range(9):
            for column in range(9):
                #if the location is different from "[0]" or is already revealed, it's not relevant for the loop.
                if solution[row][column] != "[0]" or board[row][column] == "[0]":
                    continue
                else:
                    for neighboring_row in range(row-1, row+2):
                        for neighboring_column in range(column-1, column+2):
                            if neighboring_row == -1 or neighboring_row == 9 or neighboring_column == -1 or neighboring_column == 9:
                                continue
                            elif board[neighboring_row][neighboring_column] == "[0]":
                                board[row][column] = "[0]"
                                repeat = True
                                break
    

#6 Starting the game and initiating an interactive loop:
print("______________________________________________________")
print(" ")
print("           WELCOME TO THE MINESWEEPER GAME!")
print("______________________________________________________")
print(" ")
print_board(board)
    #6.1 An initial invalid input is given, only to start the loop.
selected_r, selected_c = 9, 9

while[selected_r, selected_c] not in bombs_position:
    print(".......................................................")
    #6.2 Asking for the user's input and avoiding a bad entry error:
    try:
        selected_r, selected_c = input("Go ahead buddy, select a valid \"row/column\" value: ").split("/")
        selected_r = int(selected_r)
        selected_c = int(selected_c)
    except:
        print(" ")
        print("Are you sure this is a valid \"row/column\" value?")
        continue
    
    #6.3 In case the selected location is out of the board:
    if (selected_r > 8 or selected_r < 0) or (selected_c > 8 or selected_c < 0):
        print(" ")
        print("Hey, both row and column values should be from 0 (zero) to 8 (eight). You knew that, right?!")

    #6.4 In case the same location is chosen again:
    elif board[selected_r][selected_c] != "[ ]":
        print(" ")
        print("Hm, sorry! It looks like you have already selected this one.")
    
    #6.5 In case a bomb position is selected:
    elif [selected_r, selected_c] in bombs_position:
        board[selected_r][selected_c] = "[X]"
        print(" ")
        print_board(board)
        print(" ")
        print("Ouch, you stepted on a bomb! :(")
        print("__________________________________")
        print(" ")
        print("GAME OVER!")
        print("__________________________________")
        print(" ")
        break      
    
    #6.6 In case the selected location is safe (without a bomb):
    elif solution[selected_r][selected_c] != "[X]":
        board[selected_r][selected_c] = solution[selected_r][selected_c]
        if board[selected_r][selected_c] == "[0]":
            reveal_zeros()
        print("")
        print_board(board)
        print("")
        print("Well done, you're safe! :D")
        



    







