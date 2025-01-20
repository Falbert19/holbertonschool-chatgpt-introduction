#!/usr/bin/python3

def print_board(board):
    """Prints the Tic Tac Toe board."""
    for row in board:
        print(" | ".join(row))
        print("-" * 5)

def check_winner(board):
    """Checks if there's a winner on the board."""
    # Check rows and columns
    for row in board:
        if row.count(row[0]) == len(row) and row[0] != " ":
            return True

    for col in range(len(board[0])):
        if board[0][col] == board[1][col] == board[2][col] and board[0][col] != " ":
            return True

    # Check diagonals
    if board[0][0] == board[1][1] == board[2][2] and board[0][0] != " ":
        return True

    if board[0][2] == board[1][1] == board[2][0] and board[0][2] != " ":
        return True

    return False

def check_draw(board):
    """Checks if the game has ended in a draw (no more empty spaces)."""
    for row in board:
        if " " in row:
            return False
    return True

def tic_tac_toe():
    """Main function to play the Tic Tac Toe game."""
    board = [[" "]*3 for _ in range(3)]  # Initialize the board
    player = "X"  # Player X starts
    while True:
        print_board(board)
        row = -1
        col = -1
        
        # Get valid input for row
        while row not in [0, 1, 2]:
            try:
                row = int(input(f"Enter row (0, 1, or 2) for player {player}: "))
                if row not in [0, 1, 2]:
                    print("Invalid row. Please enter a number between 0 and 2.")
            except ValueError:
                print("Invalid input. Please enter a number.")

        # Get valid input for column
        while col not in [0, 1, 2]:
            try:
                col = int(input(f"Enter column (0, 1, or 2) for player {player}: "))
                if col not in [0, 1, 2]:
                    print("Invalid column. Please enter a number between 0 and 2.")
            except ValueError:
                print("Invalid input. Please enter a number.")
        
        # Check if the spot is taken
        if board[row][col] == " ":
            board[row][col] = player
        else:
            print("That spot is already taken! Try again.")
            continue

        # Check for a winner
        if check_winner(board):
            print_board(board)
            print(f"Player {player} wins!")
            break
        
        # Check for a draw
        if check_draw(board):
            print_board(board)
            print("The game is a draw!")
            break
        
        # Switch player
        player = "O" if player == "X" else "X"

if __name__ == "__main__":
    tic_tac_toe()
