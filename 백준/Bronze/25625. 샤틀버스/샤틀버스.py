import sys

input = sys.stdin.readline

x, y = map(int, input().strip().split())
if x > y:
    print(x + y)
else:
    print(y - x)