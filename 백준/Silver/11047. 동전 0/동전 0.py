import sys

input = sys.stdin.readline

def solve():
    n, k = map(int, input().strip().split())
    
    coins = []
    
    for i in range(n):
        coins.append(int(input().strip()))
    
    coins.sort(reverse=True)
    
    result = 0
    
    for i in range(n):
        if k // coins[i] != 0:
            result += k // coins[i]
            k = k % coins[i]
        if k == 0:
            break
        
    print(result)
    
if __name__ == "__main__":
    solve()