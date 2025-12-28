import sys

input = sys.stdin.readline

def solve():
    n, m = map(int, input().strip().split())
    arr = list(map(int, input().strip().split()))
    prefix = [0] * (n + 1)
    
    for i in range(n):
        prefix[i + 1] = prefix[i] + arr[i]

    for i in range(m):
        start, end = map(int, input().strip().split())
        result = prefix[end] - prefix[start - 1]
        print(result)
    
if __name__ == "__main__":
    solve()