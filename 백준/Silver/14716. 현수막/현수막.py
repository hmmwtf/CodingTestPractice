import sys
from collections import deque
input = sys.stdin.readline

m, n = map(int, input().strip().split())
graph = [list(map(int, input().strip().split())) for _ in range(m)]

direction = [(-1, 0), (1, 0), (0, -1), (0, 1), (-1, -1), (-1, 1), (1, -1), (1, 1)]
visited = [[False] * n for _ in range(m)]

def bfs(sx, sy):
    q = deque()
    q.append((sx, sy))
    visited[sx][sy] = True
    
    while q:
        x, y = q.popleft()
        for dx, dy in direction:
            nx, ny = x + dx, y + dy
            if 0 <= nx < m and 0 <= ny < n and graph[nx][ny] == 1 and not visited[nx][ny]:
                visited[nx][ny] = True
                q.append((nx, ny)) 
                
answer = 0
for i in range(m):
    for j in range(n):
        if graph[i][j] == 1 and not visited[i][j]:
            bfs(i,j)
            answer += 1
            
print(answer)    