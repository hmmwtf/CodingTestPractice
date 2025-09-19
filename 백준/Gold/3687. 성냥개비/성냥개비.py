import sys

input = sys.stdin.readline

dp = [float('inf')] * 101
init_list = ['', '', 1, 7, 4, 2, 6, 8]

for i in range(2, 8):
    dp[i] = init_list[i]
    
for i in range(2, 101):
    for j in range(2, i -1):
        dp[i] = min(dp[i], int(str(dp[j]) + str(dp[i - j])))
        if j == 6:
            dp[i] = min(dp[i], int(str(dp[i-j]) + '0'))
            

def find_max(num):
    result = '1' * (num // 2)
    if num % 2:
        result = '7' + result[1:]
    return result

def find_min(num):
    return dp[num]

t = int(input().strip())

for _ in range(t):
    n = int(input().strip())
    print(find_min(n), find_max(n))