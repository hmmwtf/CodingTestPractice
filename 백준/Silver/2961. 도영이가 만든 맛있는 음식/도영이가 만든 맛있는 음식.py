import sys
from itertools import combinations
input = sys.stdin.readline

n = int(input().strip())

answer = float('inf')
sour = []
bitter = []

for _ in range(n):
    s, b = map(int, input().strip().split())
    sour.append(s)
    bitter.append(b)

for r in range(1, n+1):
    for idxs in combinations(range(n), r):
        prod = 1
        summ = 0
        for i in idxs:
            prod *= sour[i]
            summ += bitter[i]
        diff = abs(prod - summ)
        if diff < answer:
            answer = diff

print(answer)