import sys, heapq
input = sys.stdin.readline
result = []

n = int(input().strip())
while True:
    x = int(input().strip())
    if x == -1:
        break
    elif x == 0:
        result.pop(0)
    else:
        if len(result) < n:
            result.append(x)

if len(result) == 0:
    print("empty")
else:
    print(" ".join(map(str, result)), end=" ")