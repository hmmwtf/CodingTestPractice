import sys
from itertools import combinations
from collections import Counter
input = sys.stdin.readline

X = input().strip()
Y = input().strip()
Z = input().strip()
k = int(input().strip())

SX = list(combinations(X, k))
SY = list(combinations(Y, k))
SZ = list(combinations(Z, k))

SA = SX + SY + SZ

counter = Counter(SA)

result = sorted(''.join(comb) for comb, cnt in counter.items() if cnt >= 2)

if not result:
    print(-1)
else:
    for comb in result:
        print(''.join(comb))