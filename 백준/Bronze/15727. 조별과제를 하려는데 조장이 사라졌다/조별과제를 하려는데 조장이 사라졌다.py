import sys

input = sys.stdin.readline

n = int(input().strip())

if n % 5 == 0:
    print(n//5)
else:
    print((n//5) + 1)