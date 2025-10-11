import sys

input = sys.stdin.readline

def solution():
    n = int(input().strip())
    arr = list(map(int, input().strip().split()))
    arr.sort()
    print(' '.join(map(str, arr)))

if __name__ == "__main__":
    solution()