import sys

input = sys.stdin.readline

def solve():
    t = int(input().strip())
    for i in range(t):
        n = int(input().strip())
        a = list(map(int, input().strip().split()))
        b = list(map(int, input().strip().split()))
        
        
        dp = [[0] * 3 for _ in range(n)]
        dp[0][0] = a[0]
        dp[0][1] = b[0]
        dp[0][2] = 0
        
        for i in range(1, n):
            dp[i][0] = max(dp[i-1][1], dp[i-1][2]) +  a[i]
            dp[i][1] = max(dp[i-1][0], dp[i-1][2]) +  b[i]
            dp[i][2] = max(dp[i-1][0], dp[i-1][1])
            
        print(max(dp[n-1][0], dp[n-1][1], dp[n-1][2]))
if __name__ == "__main__":
    solve()