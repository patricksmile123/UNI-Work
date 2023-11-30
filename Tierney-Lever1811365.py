import random

def generate_square_board():
    square_board = [[0, 0], [0, 0]]

    return (square_board)

def print_board(square_board):
    for row in square_board:
        print("| " + " | ".join(str(r) for r in row) + " |")

        print()



def generate_numbers(square_board):

    """
    :param square_board:
    generate the random numbers to replace all zeros on the board
    """
    return square_board

def calculate_win(square_board):
    message = " "
    """
    :param square_board: 
    determine a win
    message = "There is a win"
    message = "No win"
   """
    return (message)

"""
this part of the coding is for testing purposes only
"""
square_board = generate_square_board()
generate_numbers(square_board)
print_board(square_board)
message = calculate_win(square_board)