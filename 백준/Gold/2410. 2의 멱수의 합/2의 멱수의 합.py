import sys
from itertools import combinations

input = sys.stdin.readline

def solution():
    n = int(input().strip())
    MOD = 1000000000
    
    powers = []
    power = 1
    
    while power <= n:
        powers.append(power)
        power = power * 2 
    
    dp = [0] * (n + 1)
    dp[0] = 1
    
    for power in powers:
        for i in range(power, n + 1):
            dp[i] += dp[i - power]
            dp[i] %= MOD
    
    return dp[n]

if __name__ == "__main__":
    print(solution())