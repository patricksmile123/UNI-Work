def print_board(board):
    for row in range(3):
        print(board[row * 3] + '|' + board[row * 3 + 1] + '|' + board[row * 3 + 2])
        if row < 2:
            print("-----")


def check_win(board, player):
    win_conditions = [(0, 1, 2), (3, 4, 5), (6, 7, 8),
                      (0, 3, 6), (1, 4, 7), (2, 5, 8),
                      (0, 4, 8), (2, 4, 6)]
    for condition in win_conditions:
        if board[condition[0]] == board[condition[1]] == board[condition[2]] == player:
            return True
    return False


def check_tie(board):
    return all(cell != ' ' for cell in board)


def player_move(board, player):
    while True:
        try:
            move = int(input(f"Player {player}, enter a position (1-9): ")) - 1
            if 0 <= move <= 8 and board[move] == ' ':
                board[move] = player
                break
            else:
                print("Invalid move. Try again.")
        except ValueError:
            print("Invalid input. Please enter a number between 1 and 9.")

def tic_tac_toe():
    board = [' '] * 9
    current_player = 'X'
    while True:
        print_board(board)
        player_move(board, current_player)
        if check_win(board, current_player):
            print_board(board)
            print(f"Player {current_player} wins!")
            break
        if check_tie(board):
            print_board(board)
            print("It's a tie!")
            break
        current_player = 'O' if current_player == 'X' else 'X'


if __name__ == "__main__":
    tic_tac_toe()
