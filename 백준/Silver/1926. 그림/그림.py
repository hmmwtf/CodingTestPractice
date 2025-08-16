import sys
from collections import deque

input = sys.stdin.readline

n, m = map(int, input().strip().split())
board = [list(map(int, input().strip().split())) for _ in range(n)]
visited = [[False] * m for _ in range(n)]
directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

def BFS(x, y):
    q = deque()
    q.append((x, y))
    visited[x][y] = True
    area = 1
        
    while q:
        cx, cy = q.popleft()
        for dx, dy in directions:
            nx, ny = cx + dx, cy + dy
            if 0 <= nx < n and 0 <= ny < m and not visited[nx][ny] and board[nx][ny] == 1:
                visited[nx][ny] = True
                q.append((nx, ny))
                area += 1
    return area

ma = 0
p = 0

for i in range(n):
    for j in range(m):
        if board[i][j] == 1 and not visited[i][j]:
            a = BFS(i, j)
            p += 1
            if a > ma:
                ma = a
                
print(p)
print(ma)