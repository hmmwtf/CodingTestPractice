import sys
from collections import deque

input = sys.stdin.readline

def bfs(sx, sy, campus, n, m):
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    visited = [[False for _ in range(m)] for _ in range(n)]
    count = 0
    q = deque()
    
    visited[sx][sy] = True
    q.append((sx, sy))
    
    while q:
        x, y = q.popleft()
        
        if campus[x][y] == "P":
            count += 1
        
        for dx, dy in directions:
            nx = x + dx
            ny = y + dy
            if (0 <= nx < n and 
                0 <= ny < m and
                visited[nx][ny] == False and 
                (campus[nx][ny] == 'O' or campus[nx][ny] == 'P')):
                q.append((nx, ny))
                visited[nx][ny] = True
                
    return count

def solve():
    n, m = map(int, input().strip().split())
    campus = [list(input().strip()) for _ in range(n)]

    sx, sy = 0, 0
    for i in range(n):
        for j in range(m):
            if campus[i][j] == 'I':
                sx, sy = i, j
                break
    
    result = bfs(sx, sy, campus, n, m)
    
    if result == 0:
        print("TT")
    else:
        print(result)
    

if __name__ == "__main__":
    solve()