import sys
from collections import deque
input = sys.stdin.readline

n, k = map(int, input().split())


dist = [-1] * (n + 1)
dist[0] = 0
q = deque([0])

while q:
    x = q.popleft()
    if x == n:
        break

    for nx in (x + 1, x + x // 2):
        if nx <= n and dist[nx] == -1:
            dist[nx] = dist[x] + 1
            q.append(nx)

print("minigimbob" if 0 <= dist[n] <= k else "water")
