import sys

input = sys.stdin.readline

n = int(input().strip())

a = (n * 0.78)
b = (n * 0.8) + (n * 0.2 * 0.78)
print(int(a), int(b))