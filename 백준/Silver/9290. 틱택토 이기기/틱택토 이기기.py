import sys
input = sys.stdin.readline

def win(board, player):
    for i in range(3):
        for j in range(3):
            if board[i][j] == '-':
                board[i][j] = player
                if check_win(board, player):
                    return board  
                board[i][j] = '-'  
    return board  

def check_win(board, player):
    for i in range(3):
        if board[i][0] == player and board[i][1] == player and board[i][2] == player:
            return True
    for j in range(3):
        if board[0][j] == player and board[1][j] == player and board[2][j] == player:
            return True
    if board[0][0] == player and board[1][1] == player and board[2][2] == player:
        return True
    if board[0][2] == player and board[1][1] == player and board[2][0] == player:
        return True
    return False

t = int(input().strip())
for case in range(1, t + 1):
    board = [list(input().strip()) for _ in range(3)]  
    player = input().strip()
    print(f"Case {case}:")
    res = win(board, player)
    for row in res:
        print(''.join(row))  
