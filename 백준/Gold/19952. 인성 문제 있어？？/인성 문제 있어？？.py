import sys
from collections import deque

input = sys.stdin.readline

directions = [(0,1), (0, -1), (1, 0), (-1, 0)]

def bfs(h, w, o, f, xs, ys, xe, ye, obstacle):
    visited = [[[False] * (f + 1) for _ in range(w + 1)] for __ in range(h + 1)]
    queue = deque()
    queue.append((xs, ys, f))
    visited[xs][ys][f] = True

    while queue:
        x, y, power = queue.popleft()

        if x == xe and y == ye:
            return "잘했어!!"

        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if 1 <= nx <= h and 1 <= ny <= w:
                height_diff = obstacle[nx][ny] - obstacle[x][y]
                cost = 1  
                
                if height_diff <= 0:
                    if power >= cost and not visited[nx][ny][power - cost]:
                        visited[nx][ny][power - cost] = True
                        queue.append((nx, ny, power - cost))
                else:
                    if power >= cost and power >= height_diff and not visited[nx][ny][power - cost]:
                        visited[nx][ny][power - cost] = True
                        queue.append((nx, ny, power - cost))
                        
    return "인성 문제있어??"

t = int(input().strip())

for _ in range(t):
    h, w, o, f, xs, ys, xe, ye = map(int, input().strip().split())
    obstacle = [[0 for _ in range(w + 1)] for _ in range(h + 1)]
    for i in range(o):
        r, c, of = map(int, input().strip().split())
        obstacle[r][c] = of
        
    print(bfs(h, w, o, f, xs, ys, xe, ye, obstacle))
