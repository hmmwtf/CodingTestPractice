import sys

input = sys.stdin.readline

n, m = map(int, input().strip().split())
a = list(map(int, input().strip().split()))
b = list(map(int, input().strip().split()))
c = a + b
c.sort()
print(" ".join(map(str, c)))