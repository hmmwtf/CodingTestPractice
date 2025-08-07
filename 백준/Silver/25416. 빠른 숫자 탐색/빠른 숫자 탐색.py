import sys
from collections import deque

input = sys.stdin.readline

board = [list(map(int, input().strip().split())) for _ in range(5)]
r, c = map(int, input().strip().split())

directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
visited = [[False] * 5 for _ in range(5)]

def bfs(r,c):
    q = deque()
    q.append((r, c, 0))
    visited[r][c] = True

    while q:
        (x, y, dist) = q.popleft()
        
        if board[x][y] == 1:
            return dist
        
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if 0 <= nx < 5 and 0 <= ny < 5 and not visited[nx][ny] and board[nx][ny] != -1:
                visited[nx][ny] = True
                q.append((nx, ny, dist + 1))

    return -1

print(bfs(r,c))