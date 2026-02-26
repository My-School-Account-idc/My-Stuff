import sys

# Initialize board and game state
board = [' '] * 10 
player = 'X'

def display_board(b):
    print(f'\n{b[1]} | {b[2]} | {b[3]}\n--+---+--\n{b[4]} | {b[5]} | {b[6]}\n--+---+--\n{b[7]} | {b[8]} | {b[9]}\n')

def check_win(b, m):
    # Check rows, columns, and diagonals
    return ((b[1]==b[2]==b[3]==m) or (b[4]==b[5]==b[6]==m) or (b[7]==b[8]==b[9]==m) or
            (b[1]==b[4]==b[7]==m) or (b[2]==b[5]==b[8]==m) or (b[3]==b[6]==b[9]==m) or
            (b[1]==b[5]==b[9]==m) or (b[3]==b[5]==b[7]==m))

# Main game loop
print('Welcome to Tic Tac Toe!')
while True:
    display_board(board)
    try:
        move = int(input(f"Player {player}, choose a position (1-9): "))
        if 1 <= move <= 9 and board[move] == ' ':
            board[move] = player
            if check_win(board, player):
                display_board(board)
                print(f'Player {player} wins!')
                break
            if ' ' not in board[1:]:
                display_board(board)
                print("It's a tie!")
                break
            player = 'O' if player == 'X' else 'X'
        else:
            print("Invalid move. Try again.")
    except ValueError:
        print("Please enter a number 1-9.")
