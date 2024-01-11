# class Piece:
#     def __init__(self, piece_type, current_location):
#         self.piece_type = piece_type
#         self.current_location = current_location
# Pawn = Piece(Pawn, "d2")

# def print_board():
#     chess_board = [["r", "n", "b", "k", "q", "b", "n", "r"],
#                    ["p", "p", "p", "p", "p", "p", "p", "p"],
#                    [" ", " ", " ", " ", " ", " ", " ", " "],
#                    [" ", " ", " ", " ", " ", " ", " ", " "],
#                    [" ", " ", " ", " ", " ", " ", " ", " "],
#                    [" ", " ", " ", " ", " ", " ", " ", " "],
#                    ["P", "P", "P", "P", "P", "P", "P", "P"],
#                    ["R", "N", "B", "Q", "K", "B", "N", "R"]]
#     for row in chess_board:
#         for item in row:
#             print(item, end=" ")
#         print()

# print(chess_notation("b4"))