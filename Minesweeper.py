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
    board.append(["O"]*9)

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

# Creating the solution board, which will be hidden from the player:
solution = []
for i in range(9):
    solution.append(["_"]*9)
for bomb in bombs_position:
    solution[bomb[0]][bomb[1]] = "X"
for row in solution:
    for column in row:

print_board(solution)










# Starting the game and initiating an interactive loop:







