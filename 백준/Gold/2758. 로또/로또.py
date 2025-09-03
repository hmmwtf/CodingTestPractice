import sys
input = sys.stdin.readline

def lotto(n, m):
    dp = [[0] * (m + 1) for _ in range(n + 1)]
    
    for j in range(0, m + 1):
        dp[0][j] = 1
    
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            dp[i][j] = dp[i][j - 1]
            dp[i][j] += dp[i - 1][j // 2]
    
    return dp[n][m]
    

def main():
    t = int(input().strip())
    for i in range(t):
        n, m = map(int, input().strip().split())
        print(lotto(n, m))

if __name__ == "__main__":
    main()