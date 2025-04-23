import sys
from itertools import combinations

input = sys.stdin.readline

n, m = map(int, input().strip().split())

arr = [i for i in range(1, n+1)]

for comb in combinations(arr, m):
    print(" ".join(map(str, comb)))