# MINESWEEPER GAME INTRODUCTION:
print("__________________________________")
print(" ")
print("WELCOME TO THE MINESWEEPER GAME!")
print("__________________________________")

from random import randint

# Creating a null board game:
board = []
for i in range(9):
    board.append(["O"]*9)

# Function used to print the actual game board:
def print_board(board):
    for row in board:
        print (" ".join(row))

print_board(board)

# Function to generate the random positions [row, column] to the bombs:
def random_position(board):
    return [randint(0, len(board)-1), randint(0, len(board)-1)]

bomb1 = random_position(board)

print(bomb1)


