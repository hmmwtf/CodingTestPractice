import sys
from collections import deque

input = sys.stdin.readline

R, C = map(int, input().strip().split())

board = [list(input().strip()) for _ in range(R)]
directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
visited = [[False] * C for _ in range(R)]

def bfs(x, y):
    sheep = 0
    wolf = 0
    queue = deque()
    queue.append((x, y))
    visited[x][y] = True
    
    while queue:
        cx, cy = queue.popleft()
        if board[cx][cy] == 'o':
            sheep += 1
        if board[cx][cy] == 'v':
            wolf += 1
            
        for dx, dy in directions:
            nx = cx + dx
            ny = cy + dy
            
            if 0 <= nx < R and 0 <= ny < C:
                if not visited[nx][ny] and board[nx][ny] != '#':
                    queue.append((nx, ny))
                    visited[nx][ny] = True
                    
    return sheep, wolf

rs, rw = 0, 0
for i in range(R):
    for j in range(C):
        if not visited[i][j] and board[i][j] != '#':
            sheep, wolf = bfs(i, j)
            if sheep > wolf:
                rs += sheep
            else:
                rw += wolf
                
print(rs, rw)