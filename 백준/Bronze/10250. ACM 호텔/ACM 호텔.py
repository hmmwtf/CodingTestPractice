import sys

input = sys.stdin.readline

def solve(H, W, N):
    answer = 0
    if N % H == 0:
        answer = H * 100 + (N // H)
    else:
        answer = (N % H) * 100 + (N // H) + 1
    return answer

def solution():
    t = int(input().strip())
    for i in range(t):
        H, W, N = map(int, input().strip().split())
        print(solve(H, W, N))

if __name__ == "__main__":
    solution()