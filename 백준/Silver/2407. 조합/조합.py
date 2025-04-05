import sys, math
input = sys.stdin.readline
n, m = map(int, input().strip().split())
print(math.comb(n, m))