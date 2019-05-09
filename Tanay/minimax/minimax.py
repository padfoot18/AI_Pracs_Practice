def is_move_left(board):
    for row in board:
        if '_' in row:
            return True
    return False

def evaluate(board):
    for i in range(3):
        if board[i][0] == board[i][1] and board[i][1] == board[i][2]:
            if board[i][0] == 'X':
                return 100
            elif board[i][0] == 'O':
                return -100

    for i in range(3):
        if board[0][i] == board[1][i] and board[1][i] == board[2][i]:
            if board[0][i] == 'X':
                return 100
            elif board[0][i] == 'O':
                return -100

    if board[0][0] == board[1][1] and board[1][1] == board[2][2]:
        if board[0][0] == 'X':
            return 100
        elif board[0][0] == 'O': 
            return -100

    if board[0][2] == board[1][1] and board[1][1] == board[2][0]:
        if board[0][2] == 'X':
            return 100
        elif board[0][2] == 'O': 
            return -100

    return 0


def minimax(board, depth, is_max):
    score = evaluate(board)
    if is_max:
        player = 'X'
        best = -10000
    else:
        player = 'O'
        best = 10000

    if score == 100 or score == -100:
        return score - depth

    if not is_move_left(board):
        return 0

    for i in range(3):
        for j in range(3):
            if board[i][j] == '_':
                board[i][j] = player
                score = minimax(board, depth+1, not is_max)
                if is_max:
                    best = max(best, score)
                else:
                    best = min(best, score)
                board[i][j] = '_'

    return best

def best_move(board):
    if not is_move_left(board):
        print("no move remaining!")
        return

    best_score = -10000
    best_i = -1
    best_j = -1

    for i in range(3):
        for j in range(3):
            if board[i][j] == '_':
                board[i][j] = 'X'
                score = minimax(board, 0, False)
                print(f'({i}, {j}), score={score}')
                if score > best_score:
                    best_score = score
                    best_i = i
                    best_j = j
                board[i][j] = '_'
    return best_i, best_j, best_score

# print(minimax([['X', 'O', 'O'],['_', 'X', 'O'],['_', '_', '_']], 0, True))
# print(best_move([['X', 'O', 'O'],['_', 'X', 'O'],['_', '_', '_']]))

# print('Enter board position:')
board = []
for i in range(3):
    board.append(input().strip().split(' '))

print(minimax(board, 0, True))
print(best_move(board))
