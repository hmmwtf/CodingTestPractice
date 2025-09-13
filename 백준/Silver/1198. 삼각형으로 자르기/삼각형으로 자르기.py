import sys
from itertools import combinations

def solution():
    n = int(input().strip())
    board = []
    
    max_area = 0
    
    for i in range(n):
        x, y = map(int, input().strip().split())
        board.append([x, y])
    
    for i, j, k in combinations(range(n), 3):
        dx1 = board[j][0] - board[i][0]
        dy1 = board[j][1] - board[i][1]
        dx2 = board[k][0] - board[i][0]
        dy2 = board[k][1] - board[i][1]
        
        area = abs(dx1 * dy2 - dy1 * dx2) / 2.0
        
        if area > max_area:
            max_area = area
    
    print(max_area)

if __name__ == "__main__":
    solution()