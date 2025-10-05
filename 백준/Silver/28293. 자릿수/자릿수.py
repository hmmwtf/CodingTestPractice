import sys, math

input = sys.stdin.readline

def solution():
    a, b = map(int, input().strip().split())

    digits = int(b * math.log10(a)) + 1
    print(digits)

if __name__ == "__main__":
    solution()