import sys
input = sys.stdin.readline

n = int(input().strip())
m = int(input().strip())
k = int(input().strip())

print((m // n) * k)