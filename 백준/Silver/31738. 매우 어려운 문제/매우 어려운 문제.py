import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

def solution():
    n, m = map(int, input().strip().split())
    
    result = 0
    if n >= m:
        print(result)
        return
    else:
        result = 1
        for i in range(1, n + 1):
            result = (result * i) % m
    print(result)    

if __name__ == "__main__":
    solution()