import sys
from collections import deque

input = sys.stdin.readline

n = int(input().strip())

board = [list(map(int, input().strip().split())) for _ in range(n)]

directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

def BFS(x, y, h):
    q = deque()
    q.append((x,y))
    visited[x][y] = True
    
    while q:
        cx, cy = q.popleft()
        for dx, dy in directions:
            nx, ny = cx + dx, cy + dy
            if 0 <= nx < n and 0 <= ny < n and not visited[nx][ny] and board[nx][ny] > h:
                visited[nx][ny] = True
                q.append((nx, ny))

answer = 1

maxh = max(map(max, board))
minh = min(map(min, board))

for h in range(minh, maxh + 1):
    visited = [[False] * n for _ in range(n)]
    cnt = 0
    for i in range(n):
        for j in range(n):
            if not visited[i][j] and board[i][j] > h:
                BFS(i, j, h)
                cnt += 1
    answer = max(answer, cnt)
    
print(answer)