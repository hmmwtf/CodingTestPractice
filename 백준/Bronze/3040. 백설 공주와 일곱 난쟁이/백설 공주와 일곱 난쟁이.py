import sys
from itertools import combinations
input = sys.stdin.readline

a1 = int(input().strip())
a2 = int(input().strip())
a3 = int(input().strip())
a4 = int(input().strip())
a5 = int(input().strip())
a6 = int(input().strip())
a7 = int(input().strip())
a8 = int(input().strip())
a9 = int(input().strip())

arr = []

arr.append(a1)
arr.append(a2)
arr.append(a3)
arr.append(a4)
arr.append(a5)
arr.append(a6)
arr.append(a7)
arr.append(a8)
arr.append(a9)

for subset in combinations(arr, 7):
    if sum(subset) == 100:
        print('\n'.join(map(str, subset)))

