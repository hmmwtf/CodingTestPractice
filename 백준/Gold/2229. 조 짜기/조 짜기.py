import sys

input = sys.stdin.readline

def solution():
    n = int(input().strip())
    scores = list(map(int, input().strip().split()))
    
    dp = [0] * n
    
    for i in range(n):
        for j in range(i + 1):
            group_score = max(scores[j : i + 1]) - min(scores[j : i + 1])
            
            if j == 0:
                before = 0
            else:
                before = dp[j - 1]
            
            dp[i] = max(dp[i], before + group_score)
    
    print(dp[n - 1])

if __name__ == "__main__":
    solution()