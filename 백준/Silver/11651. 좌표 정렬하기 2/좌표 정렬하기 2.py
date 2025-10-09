import sys

input = sys.stdin.readline

def solution():
    n = int(input().strip())
    board = []
    
    for i in range(n):
        x, y = map(int, input().strip().split())
        board.append((x, y))
    
    board.sort(key = lambda x : (x[1], x[0]))
    for i in range(n):
        x, y = board[i]
        print(x, y)

if __name__ == "__main__":
    solution()