import sys
input = sys.stdin.readline

n = int(input().strip())
a = list(map(int, input().strip().split()))

dp = a[:]

for i in range(n):
    for j in range(i):
        if a[j] < a[i]:
            dp[i] = max(dp[i], dp[j] + a[i])
            
print(max(dp))