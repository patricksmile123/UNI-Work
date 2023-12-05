def generate_square_board():
    square_board = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

    return square_board


def print_board(square_board):
    for row in square_board:
        print("| " + " | ".join(str(r) for r in row) + " |")

        print()

current_player = "X"
def play():
    which_box = input("Where would you like to play?, select from 1 to 9")


print_board(generate_square_board())


