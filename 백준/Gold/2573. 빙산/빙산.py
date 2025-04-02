import sys
input = sys.stdin.readline

n, m = map(int, input().strip().split())
graph =[list(map(int, input().strip().split())) for _ in range(n)]
time = 0
direction = [(-1, 0), (1, 0), (0, -1), (0, 1)]

def DFS(x, y):
    stack = [(x, y)]
    visited[x][y] = 1
    
    while stack:
        cx, cy = stack.pop()
        for dx, dy in direction:
            nx, ny = cx + dx, cy + dy
            if 0 <= nx < n and 0 <= ny < m:
                if graph[nx][ny] == 0:
                    visited[cx][cy] += 1
                elif graph[nx][ny] > 0 and visited[nx][ny] == 0:
                    visited[nx][ny] = 1
                    stack.append((nx, ny))

while True:
    cnt = 0
    visited = [[0] *m for _ in range(n)]
    
    for i in range(n):
        for j in range(m):
            if graph[i][j] > 0 and visited[i][j] == 0:
                DFS(i, j)
                cnt += 1
    
    if cnt >= 2:
        print(time)
        break
    if cnt == 0:
        print(0)
        break
    
    for i in range(n):
        for j in range(m):
            if visited[i][j] != 0:
                graph[i][j] -= (visited[i][j] - 1)
                if graph[i][j] < 0:
                    graph[i][j] = 0
                    
    time += 1