import sys
input = sys.stdin.readline

n = int(input().strip())

dp = [float('inf')] * (n + 1)
dp[0] = 0

for x in range(1, n+1):
    for i in range(1, int(x**(0.5)) + 1):
        isqrt = i ** (2)
        if isqrt <= x:
            dp[x] = min(dp[x], dp[x-isqrt] + 1)
            
print(dp[n])