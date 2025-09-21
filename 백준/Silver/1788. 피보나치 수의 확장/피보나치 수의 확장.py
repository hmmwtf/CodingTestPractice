import sys

input = sys.stdin.readline

def solution():
    n = int(input().strip())
    
    if n == 0:
        print(0)
        print(0)
        return
    elif n > 0:
        dp = [0] * (n+1)
        dp[0] = 0
        dp[1] = 1
    
        for i in range(2, n + 1):
            dp[i] = (dp[i - 1] + dp[i - 2]) % 1000000000
        print(1)
        print(dp[n])
    else:
        pn = abs(n)
        dp = [0] * (pn+1)
        dp[0] = 0
        dp[1] = 1
    
        for i in range(2, pn + 1):
            dp[i] = (dp[i - 1] + dp[i - 2]) % 1000000000
        
        if pn % 2 == 0:
            print(-1)
        else:
            print(1)
        print(dp[pn])
    
if __name__ == "__main__":
    solution()