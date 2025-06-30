import sys

input = sys.stdin.readline

n = int(input().strip())

dp = [0 for _ in range(n+1)]
for i in range(1, n + 1):
    dp[i] = float('inf')
    for coin in [1, 2, 5, 7]:
        if i - coin >= 0:
            dp[i] = min(dp[i], dp[i - coin] + 1)
print(dp[n])