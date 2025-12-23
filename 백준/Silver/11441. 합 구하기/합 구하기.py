import sys

input = sys.stdin.readline

def solution():
    
    n = int(input().strip())
    nums = list(map(int, input().strip().split()))
    m = int(input().strip())
    
    prefix = [0] * (n + 1)
    
    for i in range(n):
        prefix[i + 1] = prefix[i] + nums[i]
    
    for i in range(m):
        start, end = map(int, input().strip().split())
        result = prefix[end] - prefix[start - 1]
        print(result)

if __name__ == "__main__":
    solution()