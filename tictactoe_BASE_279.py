def init_board():
    board = [ [ '.','.','.' ],[ '.','.','.' ],[ '.','.','.' ] ]  
    return board

def get_move(board, player):
    is_looping = True
    coordinates_dict = {"A1" : [0,0], "A2" : [0,1], "A3" : [0,2], "B1" : [1,0], "B2" : [1,1], "B3" : [1,2], "C1" : [2,0], "C2" : [2,1], "C3" : [2,2]}
    while is_looping:
        user_input_coordinates = (input("Please provide coordinates for player " + player + " as RowCol: ")).upper()
        if user_input_coordinates == "quit":
            print("Goodbye!")
            break
        elif user_input_coordinates in coordinates_dict:
            raw_coordinates = (coordinates_dict[user_input_coordinates])
            row, col = int(raw_coordinates[0]), int(raw_coordinates[1])
            if (board[row][col] == '.'):
                return row, col
        else:
            print("Try again!")

def get_ai_move(board, player):
    """Returns the coordinates of a valid move for player on board."""
    row, col = 0, 0
    return row, col
    pass

def has_won(board, player):
    win_board = [
        board[0], board[1], board[2],
        [board[0][0], board[1][0], board[2][0]],
        [board[0][1], board[1][1], board[2][1]],
        [board[0][2], board[1][2], board[2][2]],
        [board[0][0], board[1][1], board[2][2]],
        [board[2][0], board[1][1], board[0][2]],
    ]
    if [player, player, player] in win_board:
        return True
    else:
        return False 

def mark(board, player, row, col):
    if board[row][col] == '.':
        board[row][col] = player
    else:
        get_move(board, player)

def is_full(board):
    if ('.' in board == False):
       return True
    else:
        return False

def print_board(board):
    coordinate_board = ["A", "B", "C", "---+---+---", " 1   2   3  ", "  "]
    print("".join(coordinate_board[5]), "".join(coordinate_board[4]))
    for i in range ((len(board)-1)):
        print(coordinate_board[i]," ",  " | ".join(board[i]))
        print(coordinate_board[5], coordinate_board[3])
    print(coordinate_board[2]," ", " | ".join(board[2]))
    
def print_result(winner):
    if winner == "X" or winner == "O":  
        print(winner.upper() +" has won!")
    else:
        print("It's a tie!")

def tictactoe_game(mode='HUMAN-HUMAN'):
    board = init_board()
    player = "X"
    winner = 0
    while True:
        print_board(board)
        row, col = get_move(board, player)
        mark(board, player, row, col)
        if has_won(board, player):
            winner = player
            print_board(board)
            print_result(winner)
            break
        elif is_full(board):
            print_result(winner)
            break
        player = "O" if player == "X" else "X"
        

tictactoe_game(mode='HUMAN-HUMAN')