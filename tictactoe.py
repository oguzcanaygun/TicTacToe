from IPython.display import clear_output

def display_board(board):
    clear_output()
    print(f' {board[7]} | {board[8]} | {board[9]} ')
    print(f' {board[4]} | {board[5]} | {board[6]} ')
    print(f' {board[1]} | {board[2]} | {board[3]} ')

test_board = ['#','X','O','X','O','X','O','X','O','X']
display_board(test_board)

def player_input():
    
    marker = ""
    while marker != "X" and marker != "O":
        market = input("Player 1: Choose X or O: ").upper()

    if market == "X":
        return ("X", "O")
    else:
        return ("O","X")
    
def place_marker(board, marker, position):
    
    board[position] = marker

print(test_board)
place_marker(test_board,'$',8)
display_board(test_board)
