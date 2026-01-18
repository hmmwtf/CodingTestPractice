import sys

input = sys.stdin.readline

def solve():
    n, k = map(int, input().strip().split())
    W, V = [], []
    
    dp = [[0] * (k + 1) for _ in range(n + 1)]
    
    for i in range(n):
        w, v = map(int, input().strip().split())
        W.append(w)
        V.append(v)
    
    for i in range(1, n + 1):
        for w in range(k + 1):
            if w >= W[i - 1]:
                dp[i][w] = max(dp[i-1][w], dp[i-1][w - W[i - 1]] + V[i - 1])
            else:
                dp[i][w] = dp[i-1][w]
    
    print(dp[n][k])
    
if __name__ == "__main__":
    solve()