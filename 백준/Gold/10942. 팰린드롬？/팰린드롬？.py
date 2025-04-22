import sys
input = sys.stdin.readline

def build_dp(arr):
    n = len(arr)
    dp = [[0]*n for _ in range(n)]
    
    for i in range(n):
        dp[i][i] = 1
    
    for i in range(n-1):
        if arr[i] == arr[i+1]:
            dp[i][i+1] = 1
    
    for length in range(3, n+1):
        for i in range(n-length+1):
            j = i + length - 1
            if arr[i] == arr[j] and dp[i+1][j-1]:
                dp[i][j] = 1
    
    return dp

def Pal(dp, start, end):
    return dp[start][end]

n = int(input().strip())
arr = list(map(int, input().split()))
dp = build_dp(arr)

m = int(input().strip())
for _ in range(m):
    s, e = map(int, input().split())
    print(Pal(dp, s-1, e-1))