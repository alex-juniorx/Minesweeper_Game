#MINESWEEPER GAME
#Game played on terminal on a 9x9 Board, with 16 Bombs, enumerated neighboring positions and final score (based on revealed positions and elapsed time)

import time
from random import randint

#1 INITIAL BOARD IS CREATED:
board = []

for i in range(9):
    board.append(["[ ]"]*9)

#2 FUNCTION USED TO PRINT THE ACTUAL GAME BOARD (WITH NUMBERED ROWS AND COLUMNS):
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

#3 BOMB POSITIONS ARE GENERATED (NON-DUPLICATE VALUES)::
bombs_position = []

for i in range(15):
    temp_position = [randint(0, len(board)-1), randint(0, len(board)-1)]
    while temp_position in bombs_position:
        temp_position = [randint(0, len(board)-1), randint(0, len(board)-1)]
    bombs_position.append(temp_position)

#4 SOLUTION BOARD IS CREATED FOR REFERENCE ALONG THE GAME (IT IS HIDDEN FROM THE PLAYER):
solution = []

    #4.1 Default value "[ ]" is positioned in the initial positions:
for i in range(9):
    solution.append(["[ ]"]*9)
    
    #4.2 "[X]" values are placed in the defined bomb positions:
for bomb in bombs_position:
    solution[bomb[0]][bomb[1]] = "[X]"
    
    #4.3 Positions are enumerated based on neighboring bombs (except for bomb positions).
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

#5 FUNCTION CREATED TO REVEAL "[0]" LOCATIONS, WHEN A NEIGHBORING "[0]" IS REVEALED BY THE PLAYER:
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

#6 FUNCTION USED TO CALCULATE THE FINAL SCORE BASED ON THE NUMBER OF REVEALED SAFE POSITIONS AND ELAPSED TIME
def final_score(elapsed_time):
    final_score = 0
    for row in range(9):
        for column in range(9):
            if board[row][column] != "[X]" and board[row][column] != "[ ]":
                final_score += 10
    if elapsed_time < 60:
        final_score += 350
    elif elapsed_time < 120:
        final_score += 250
    elif elapsed_time < 180:
        final_score += 150
    elif elapsed_time < 240:
        final_score += 50
    return final_score


#7 THE GAME’S INTERACTIVE LOOP IS INITIALIZED::
print("______________________________________________________")
print(" ")
print("           WELCOME TO THE MINESWEEPER GAME!")
print("______________________________________________________")
print(" ")
print_board(board)
    #7.1 The timer is started and an initial invalid input is given (only to start the loop):
t0 = time.time()
selected_r, selected_c = 9, 9

while[selected_r, selected_c] not in bombs_position:
    print(".......................................................")
    #7.2 User's input is demanded (bad entry error prevented):
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
        elapsed_time = time.time() - t0
        print("__________________________________")
        print(" ")
        print("GAME OVER!")
        print("FINAL SCORE: ", str(final_score(elapsed_time)))
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
        



    







