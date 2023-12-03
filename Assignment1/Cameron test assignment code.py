import random

def generate_square_board():

    """
    change square_board above to reflect the 2 X 2 board
    insert code here to generate a square board of 2 X 2 with zeros
    """
    square_board = [0, 0, 0, 0]

    return square_board

def print_board(square_board):
    """
    :param square_board:
    print the board as instructed
    """
    print("|", square_board[0], "|", square_board[1], "|\n|", square_board[2], "|", square_board[3], "|")

def generate_numbers(square_board):
    """
    :param square_board:
    generate the random numbers to replace all zeros on the board
    """
    for i in range(len(square_board)):
        square_board[i] = random.randint(1, 20)
    return square_board

def calculate_win(square_board):
    message = " "
    """
    :param square_board:
    determine a win
    message = "There is a win"
    message = "No win"
    """
    value = 0
    for i in range(len(square_board)-1):
        value += square_board[i]

    if value % 10 == 0:
        message = "There is a win"
    else:
        message = "No win"
    return message

"""
this part of the coding is for testing purposes only
"""
square_board = generate_square_board()
generate_numbers(square_board)
print_board(square_board)
message = calculate_win(square_board)
print(message)