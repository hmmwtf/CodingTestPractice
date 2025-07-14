import sys
from collections import deque

input = sys.stdin.readline

n, m, k = map(int, input().strip().split())

board = [[0] * (m + 1) for _ in range(n + 1)]
visit = [[False] * (m + 1) for _ in range(n + 1)]
directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
max_size = 0

def bfs(x, y):
    q = deque()
    q.append((x, y))
    visit[x][y] = True
    size = 1
    
    while q:
        cx, cy = q.pop()
        for dx, dy in directions:
            nx = cx + dx
            ny = cy + dy
            if 1 <= nx <= n and 1 <= ny <= m and board[nx][ny] == 1 and not visit[nx][ny]:
                q.append((nx, ny))
                visit[nx][ny] = True
                size += 1
    return size

for i in range(k):
    r, c = map(int, input().strip().split())
    board[r][c] = 1
    
for i in range(1, n + 1):
    for j in range(1, m + 1):
        if board[i][j] == 1 and not visit[i][j]:
            size = bfs(i, j)
            max_size = max(max_size, size)

print(max_size)