import random


def generate_square_board():
    square_board = [[0, 0], [0, 0]]

    return square_board


def print_board(square_board):
    for row in square_board:
        print("| " + " | ".join(str(r) for r in row) + " |")

        print()


def generate_numbers(square_board):
    square_board[0][0] = random.randint(1,20)
    square_board[0][1] = random.randint(1,20)
    square_board[1][0] = random.randint(1,20)
    square_board[1][1] = random.randint(1,20)
    # for y in range(len(square_board)):
    #     for x in range(len(square_board[y])):
    #         square_board[y][x] = random.randint(1,20)

    """
    :param square_board:
    generate the random numbers to replace all zeros on the board
    """
    return square_board


def calculate_win(square_board):
    # total = 0
    # for row in square_board:
    #     for column in row:
    #         total += column

    total = square_board[0][0] + square_board[0][1] + square_board[1][0] + square_board[1][1]
    if total % 10 == 0:
        return "There is a win"
    else:
        return "No win"


"""
this part of the coding is for testing purposes only
"""
square_board = generate_square_board()
generate_numbers(square_board)
print_board(square_board)
message = calculate_win(square_board)
print(message)