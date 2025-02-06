import random

def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 9)

def check_winner(board):
    # Check rows, columns, and diagonals
    for row in board:
        if row[0] == row[1] == row[2] and row[0] != " ":
            return row[0]
    
    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col] and board[0][col] != " ":
            return board[0][col]
    
    if board[0][0] == board[1][1] == board[2][2] and board[0][0] != " ":
        return board[0][0]
    
    if board[0][2] == board[1][1] == board[2][0] and board[0][2] != " ":
        return board[0][2]
    
    return None

def is_full(board):
    return all(cell != " " for row in board for cell in row)

def get_available_moves(board):
    return [(r, c) for r in range(3) for c in range(3) if board[r][c] == " "]

def minimax(board, depth, is_maximizing):
    winner = check_winner(board)
    if winner == "O":
        return 1
    elif winner == "X":
        return -1
    elif is_full(board):
        return 0
    
    if is_maximizing:
        best_score = -float('inf')
        for move in get_available_moves(board):
            board[move[0]][move[1]] = "O"
            score = minimax(board, depth + 1, False)
            board[move[0]][move[1]] = " "
            best_score = max(score, best_score)
        return best_score
    else:
        best_score = float('inf')
        for move in get_available_moves(board):
            board[move[0]][move[1]] = "X"
            score = minimax(board, depth + 1, True)
            board[move[0]][move[1]] = " "
            best_score = min(score, best_score)
        return best_score

def ai_move(board):
    best_score = -float('inf')
    best_move = None
    for move in get_available_moves(board):
        board[move[0]][move[1]] = "O"
        score = minimax(board, 0, False)
        board[move[0]][move[1]] = " "
        if score > best_score:
            best_score = score
            best_move = move
    board[best_move[0]][best_move[1]] = "O"

def player_move(board):
    while True:
        try:
            move = input("Enter your move (row and column: 1-3 1-3): ").split()
            r, c = int(move[0]) - 1, int(move[1]) - 1
            if (r, c) in get_available_moves(board):
                board[r][c] = "X"
                break
            else:
                print("Invalid move! Try again.")
        except (ValueError, IndexError):
            print("Invalid input! Enter row and column as numbers from 1 to 3.")

def main():
    board = [[" " for _ in range(3)] for _ in range(3)]
    print("Tic-Tac-Toe AI - You are 'X', AI is 'O'")
    
    while True:
        print_board(board)
        player_move(board)
        
        if check_winner(board):
            print_board(board)
            print("You win! 🎉")
            break
        elif is_full(board):
            print_board(board)
            print("It's a draw!")
            break
        
        ai_move(board)
        
        if check_winner(board):
            print_board(board)
            print("AI wins! 🤖")
            break
        elif is_full(board):
            print_board(board)
            print("It's a draw!")
            break

if __name__ == "__main__":
    main()
