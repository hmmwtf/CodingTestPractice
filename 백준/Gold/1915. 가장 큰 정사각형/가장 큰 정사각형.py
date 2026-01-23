import sys

input = sys.stdin.readline

def solve():
    n, m = map(int, input().strip().split())
    board = [list(map(int, input().strip())) for _ in range(n)]
    dp = [[0] * m for _ in range(n)]
    
    for i in range(n):
        for j in range(m):
            if board[i][j] == 0:
                dp[i][j] = 0
            elif i == 0 or j == 0:
                dp[i][j] = 1
            else:
                dp[i][j] = min(dp[i-1][j], dp[i-1][j-1], dp[i][j-1]) + 1
    
    answer = max(max(row) for row in dp)
    print(answer * answer)
    
if __name__ == "__main__":
    solve()