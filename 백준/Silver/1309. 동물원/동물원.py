import sys
input = sys.stdin.readline

n = int(input().strip())
dp = [[0] * 3 for _ in range(n+1)]
dp[1][0] = 1
dp[1][1] = 1
dp[1][2] = 1
MOD = 9901
for i in range(2, n+1):
    dp[i][0] = (dp[i-1][0] + dp[i-1][1] + dp[i-1][2]) % MOD
    dp[i][1] = (dp[i-1][0] + dp[i-1][2]) % MOD
    dp[i][2] = (dp[i-1][0] + dp[i-1][1]) % MOD
    
answer = (dp[n][0] + dp[n][1] + dp[n][2]) % MOD
print(answer)