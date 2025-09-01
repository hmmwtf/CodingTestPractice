import sys
import bisect
input = sys.stdin.readline

def solution():
    n = int(input().strip())
    board = []
    for i in range(n):
        x, y = map(int, input().strip().split())
        board.append((x, y))
    
    gradients = []
    for i in range(0, n-1):
        gradient = (board[i + 1][1] - board[i][1]) / (board[i + 1][0] - board[i][0]) 
        gradients.append(gradient)
    
    xs = [board[i][0] for i in range(n)]
    q = int(input().strip())
    for i in range(q):
        k = float(input().strip())
        idx = bisect.bisect_left(xs, k) - 1
        if gradients[idx] == 0:
            print(0)
        else:
            if gradients[idx] > 0:
                print(1)
            else:
                print(-1)
                    
if __name__ == "__main__":
    solution()