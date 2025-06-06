import sys

input = sys.stdin.readline

n = int(input().strip())
arr = list(map(int, input().strip().split()))

dp = [0] * n
dp[0] = arr[0]

for i in range(1, n):
    dp[i] = max(arr[i], dp[i-1] + arr[i])
    
print(max(dp))