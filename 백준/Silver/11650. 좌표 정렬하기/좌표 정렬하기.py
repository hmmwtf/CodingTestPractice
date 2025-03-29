import sys
input = sys.stdin.readline

n = int(input().strip())
board = [list(map(int, input().strip().split())) for _ in range(n)]
board.sort(key=lambda point: (point[0], point[1]))
for i in range(n):
    print(" ".join(map(str,board[i])))