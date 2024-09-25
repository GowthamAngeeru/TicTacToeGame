def print_board(board):
    print("\n")
    print(f"{board[0]} | {board[1]} | {board[2]}")
    print("--+---+--")
    print(f"{board[3]} | {board[4]} | {board[5]}")
    print("--+---+--")
    print(f"{board[6]} | {board[7]} | {board[8]}")
    print("\n")

def check_win(board, player):
    win_combinations = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8], # rows
        [0, 3, 6], [1, 4, 7], [2, 5, 8], # columns
        [0, 4, 8], [2, 4, 6]             # diagonals
    ]
    for combo in win_combinations:
        if all(board[i] == player for i in combo):
            return True
    return False

def check_tie(board):
    return all(spot != " " for spot in board)

def play_game():
    board = [" "] * 9
    current_player = "X"
    
    while True:
        print_board(board)
        move = input(f"Player {current_player}, enter your move (1-9): ")
        
        try:
            move = int(move) - 1
            if board[move] != " ":
                print("Spot already taken. Try again.")
                continue
        except (ValueError, IndexError):
            print("Invalid move. Try again.")
            continue
        
        board[move] = current_player
        
        if check_win(board, current_player):
            print_board(board)
            print(f"Player {current_player} wins!")
            break
        elif check_tie(board):
            print_board(board)
            print("It's a tie!")
            break
        
        current_player = "O" if current_player == "X" else "X"

if __name__ == "__main__":
    play_game()
