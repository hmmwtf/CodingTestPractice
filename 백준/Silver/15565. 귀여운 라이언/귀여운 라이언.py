import sys

input = sys.stdin.readline

n, k = map(int, input().strip().split())
dolls = list(map(int, input().strip().split()))

left, right = 0, 0
cnt = 0
minLen = float("INF")

for right in range(0, n):
    if dolls[right] == 1:
        cnt += 1
        
    while cnt >= k:
        minLen = min(minLen, right - left + 1)
        if dolls[left] == 1:
            cnt -= 1
        left += 1
        
if minLen == float("INF"):
    print(-1)
else:
    print(minLen)