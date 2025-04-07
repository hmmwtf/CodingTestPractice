import sys
input = sys.stdin.readline

n = int(input().strip())
matrices = []

for _ in range(n):
    r, c = map(int, input().strip().split())
    matrices.append((r, c))
    
dp = [[0] * n for _ in range(n)]

for length in range(2, n+1):
    for start in range(n - length + 1):
        end = start + length - 1
        dp[start][end] = float('inf')
        
        for k in range(start, end):
            cost = (dp[start][k] +
                    dp[k+1][end]+ 
                    matrices[start][0] * matrices[k][1] * matrices[end][1])
            dp[start][end] = min(dp[start][end], cost)

print(dp[0][n-1])