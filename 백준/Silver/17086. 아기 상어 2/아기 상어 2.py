import sys
from collections import deque
input = sys.stdin.readline

n, m = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]
directions = [(-1, 0), (1, 0), (0, -1), (0, 1), (-1, -1), (-1, 1), (1, -1), (1, 1)]

dif = [[0]*m for _ in range(n)]
max_dist = 0

for i in range(n):
    for j in range(m):
        if graph[i][j] != 0:
            continue

        visited = [[False]*m for _ in range(n)]
        q = deque([(i, j, 0)])
        visited[i][j] = True

        found = False
        while q and not found:
            x, y, dist = q.popleft()
            for dx, dy in directions:
                nx, ny = x + dx, y + dy
                if not (0 <= nx < n and 0 <= ny < m):
                    continue
                if visited[nx][ny]:
                    continue
                visited[nx][ny] = True

                if graph[nx][ny] == 1:
                    dif[i][j] = dist + 1
                    max_dist = max(max_dist, dist + 1)
                    found = True
                    break
                else:
                    q.append((nx, ny, dist + 1))

print(max_dist)