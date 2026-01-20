import sys

input = sys.stdin.readline

def solve():
    n, k = map(int, input().strip().split())
    coins = []
    for i in range(n):
        cv = int(input().strip())
        coins.append(cv)
    dp = [0] * (k + 1)
    dp[0] = 1
    
    for c in coins:
        for j in range(c, k + 1):
            dp[j] += dp[j - c]

    print(dp[k])
if __name__ == "__main__":
    solve()