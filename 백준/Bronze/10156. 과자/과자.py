import sys

input = sys.stdin.readline

k, n, m = map(int, input().strip().split())

if (k * n) > m:
    print((k * n) - m)
else:
    print(0)    