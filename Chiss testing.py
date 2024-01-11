class Piece:
    def __init__(self, piece_type, current_location):
        self.piece_type = piece_type
        self.current_location = current_location
Pawn = Piece(Pawn, "d2")