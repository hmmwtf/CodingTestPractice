import sys

input = sys.stdin.readline

def cnt_repaint(board, start_row, start_col, first_color):
    cnt = 0
    for i in range(start_row, start_row + 8):
        for j in range(start_col, start_col + 8):
            if (i + j) % 2 == 0:
                expect_color = first_color
            else:
                expect_color = 'B' if first_color == 'W' else 'W'
            
            if board[i][j] != expect_color:
                cnt += 1
    return cnt

def solution():
    n, m = map(int, input().strip().split())
    board = [list(input().strip()) for _ in range(n)]
    
    min_repaint = float('inf')
    
    for i in range(0, n - 7):
        for j in range(0, m - 7):
            p1 = cnt_repaint(board, i, j, 'W')
            p2 = cnt_repaint(board, i, j, 'B')
            
            min_repaint = min(min_repaint, min(p1, p2))

    print(min_repaint)

if __name__ == "__main__":
    solution()