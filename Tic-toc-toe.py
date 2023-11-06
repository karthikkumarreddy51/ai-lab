import random
def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 9)
def check_winner(board, player):
    for row in board:
        if all(cell == player for cell in row):
            return True
    for col in range(3):
        if all(board[row][col] == player for row in range(3)):
            return True
    if all(board[i][i] == player for i in range(3)) or all(board[i][2 - i] == player for i in range(3)):
        return True
    return False
def find_empty_cells(board):
    empty_cells = []
    for row in range(3):
        for col in range(3):
            if board[row][col] == " ":
                empty_cells.append((row, col))
    return empty_cells
def computer_move(board):
    empty_cells = find_empty_cells(board)  
    # Magic square strategy
    magic_square = [
        [8, 1, 6],
        [3, 5, 7],
        [4, 9, 2]
    ]
    best_move = None
    best_score = -1  
    for row, col in empty_cells:
        score = magic_square[row][col]
        if score > best_score:
            best_score = score
            best_move = (row, col)  
    return best_move
def main():
    board = [[" " for _ in range(3)] for _ in range(3)]
    player = "X"
    computer = "O"
    game_over = False  
    print("Welcome to Tic-Tac-Toe!")
    print_board(board)  
    while not game_over:
        if player == "X":
            row, col = map(int, input("Enter your move (row and column): ").split())
        else:
            row, col = computer_move(board)
            print("Computer's move:", row, col) 
        if board[row][col] == " ":
            board[row][col] = player
            print_board(board)
            if check_winner(board, player):
                print(player, "wins!")
                game_over = True
            elif all(board[r][c] != " " for r in range(3) for c in range(3)):
                print("It's a draw!")
                game_over = True
            player = "X" if player == "O" else "O"
        else:
            print("Cell is already occupied. Try again.")
if __name__ == "__main__":
    main()