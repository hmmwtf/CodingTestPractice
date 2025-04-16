import sys
from collections import Counter

input = sys.stdin.readline

n = int(input().strip())
a = list(map(int, input().strip().split()))
m = int(input().strip())
b = list(map(int, input().strip().split()))

count = Counter(a)

result = []
for num in b:
    result.append(str(count[num]))
    
print(" ".join(result))