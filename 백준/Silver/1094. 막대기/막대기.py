import sys
from itertools import combinations
input = sys.stdin.readline

x = int(input().strip())

factors = [64, 32, 16, 8, 4, 2, 1]

result = []
for r in range(1, len(factors) + 1):
    for com in combinations(factors, r):
        if x == sum(com):
            result.append(len(com))
            
print(min(result))