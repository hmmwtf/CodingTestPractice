import sys
from collections import deque

input = sys.stdin.readline

n = int(input().strip())

direction = [(-2, -1), (-2, 1), (0, -2), (0, 2), (2, -1), (2, 1)]

r1, c1, r2, c2 = map(int, input().strip().split())

visited = [[False for _ in range(n)] for _ in range(n)]

q = deque()
q.append((r1, c1, 0))
visited[r1][c1] = True

answer = -1

while q:
    nowr, nowc, cnt = q.popleft()
    
    if nowr == r2 and nowc == c2:
        answer = cnt
        break
    
    for dr, dc in direction:
        nextr = nowr + dr
        nextc = nowc + dc
        
        if 0 <= nextr < n and 0<= nextc < n and not visited[nextr][nextc]:
            visited[nextr][nextc] = True
            q.append((nextr, nextc, cnt + 1))

print(answer)