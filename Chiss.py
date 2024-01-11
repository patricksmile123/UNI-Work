

# import sys
# def main():
#     while True:
#         if check_checkmate() == True:
#             print(f"The game is over, {winner} has won.")
#             sys.exit()
#         elif check_check() == True:
#             print("One of the players is in check")
#             print_board()
#         else print_board():
#         current_turn = 0
#         if current_turn % 2 == 0:
#             print("White to play")
#         else
#             print("Black to play")
#         current_turn += 1
#         piece_location(input("What move do you wish to make"))


def print_board():
    chess_board = [["r", "n", "b", "k", "q", "b", "n", "r"], ["p", "p", "p", "p", "p", "p", "p", "p"],
                   [" ", " ", " ", " ", " ", " ", " ", " "], [" ", " ", " ", " ", " ", " ", " ", " "],
                   [" ", " ", " ", " ", " ", " ", " ", " "], [" ", " ", " ", " ", " ", " ", " ", " "],
                   ["P", "P", "P", "P", "P", "P", "P", "P"], ["R", "N", "B", "Q", "K", "B", "N", "R"]]
    for row in chess_board:
        for item in row:
            print(item, end=" ")
        print()


def move_piece(piece_location):
    find_piece()

def find_piece(move):
    piece_location = ""
    if len(move) == 2:
        row = move[0]
        column = move[1]
    elif len(move) == 3:
        piece = move[0]
        row = move[1]
        column = move[2]
    elif len(move) == 4:
        piece = move[0]
        take = move[1]
        row = move[2]
        column = move[3]
    if len(move) == 4 and take != "x":
        which_piece = [1]
