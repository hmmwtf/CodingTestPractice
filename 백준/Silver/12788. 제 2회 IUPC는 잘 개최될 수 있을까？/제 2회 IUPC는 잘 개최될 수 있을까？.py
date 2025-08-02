import sys
from itertools import combinations

input = sys.stdin.readline

n = int(input().strip())
m, k = map(int, input().strip().split())
a = list(map(int, input().strip().split()))

total = m * k

if sum(a) < total:
    print("STRESS")
else:
    a.sort(reverse=True)
    result = 0
    for idx, pen in enumerate(a, 1):
        result += pen
        if result >= total:
            print(idx)
            break
        