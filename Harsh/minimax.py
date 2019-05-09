from pprint import pprint

def is_moves_left():
    """
    This function returns true if there are moves remaining on the board. It returns false if
    there are no moves left to play.
    :return: boolean
    """
    for i in range(3):
        for j in range(3):
            if board[i][j] == '_':
                return True
    return False
    

def evaluation_function():
    # Checking rows
    for row in range(3):
        if board[row][0] == board[row][1] and board[row][0] == board[row][2]:
            if board[row][0] == 'X':
                return 10
            elif board[row][0] == 'O':
                return -10

    # Checking columns
    for col in range(3):
        if board[0][col] == board[1][col] and board[0][col] == board[2][col]:
            if board[col][col] == 'X':
                return 10
            elif board[col][col] == 'O':
                return -10

    # Checking diagonals
    if board[0][0] == board[1][1] and board[1][1] == board[2][2]:
        if board[0][0] == 'X':
            return 10
        elif board[0][0] == 'O':
            return -10

    if board[0][2] == board[1][1] and board[1][1] == board[2][0]:
        if board[0][2] == 'X':
            return 10
        elif board[0][2] == 'O':
            return -10

    return 0


def minimax(is_max, depth):
    """
    Considers all the possible ways the game can go and returns the value of the board
    :return: value: int
    """
    score = evaluation_function()
    if score == 10 or score == -10 or not is_moves_left():
        return score

    if is_max:
        best = -1000
        for i in range(3):
            for j in range(3):
                if board[i][j] == '_':
                    board[i][j] = 'X'
                    best = max(best, minimax(not is_max, depth + 1))
                    board[i][j] = '_'
        return best
    else:
        best = 1000
        for i in range(3):
            for j in range(3):
                if board[i][j] == '_':
                    board[i][j] = 'O'
                    best = min(best, minimax(not is_max, depth + 1))
                    board[i][j] = '_'
        return best


def find_best_move():
    """
    Return best possible move for the player
    """
    best_value = -1000
    best_move_row = -1
    best_move_column = -1
    for i in range(3):
        for j in range(3):
            if board[i][j] == '_':
                board[i][j] = 'X'
                move_value = minimax(False, 0)
                print('Move Position: (', str(i+1), ',', str(j+1), ')  Heuristic Score = ', str(move_value))
                board[i][j] = '_'
                if move_value > best_value:
                    best_move_row = i
                    best_move_column = j
                    best_value = move_value
    return best_move_column, best_move_row, best_value

def display(board):
    for i in range (0,3):
        for j in range(0,3):
            print(board[i][j], end=" ")
        print("\n")

if __name__ == '__main__':
    board = []
    print('Enter board state:')
    for i in range(3):
        input_lines = input('')
        board.append(input_lines.strip().split())
    
    X_player = True
    while is_moves_left() and evaluation_function() != 10:
        if X_player:    
            move_column, move_row, value = find_best_move()
            board[move_row][move_column] = 'X'
            print('Best row move', str(move_row))
            print('Best column move', str(move_column))
            print('Score', str(value))
            print('-----BOARD STATE-----')
            display(board)
            X_player = False
        else:
               enter_row, enter_col = input("Enter move\n").split(' ')
               board[int(enter_row)-1][int(enter_col)-1] = 'O'
               X_player = True