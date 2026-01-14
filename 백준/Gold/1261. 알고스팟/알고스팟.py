import sys
from collections import deque

input = sys.stdin.readline

def bfs(n, m, maze):
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    q = deque()
    visited = [[False] * m for _ in range(n)]
    
    q.append((0, 0, 0))
    visited[0][0] = True
    
    while q: 
        x, y, walls = q.popleft()
        
        if x == n - 1 and y == m - 1:
            return walls
        
        for dx, dy in directions:
            nx = x + dx
            ny = y + dy
            
            if 0 <= nx < n and 0 <= ny < m and visited[nx][ny] == False:
                visited[nx][ny] = True
                if maze[nx][ny] == 0:
                    q.appendleft((nx, ny, walls))
                if maze[nx][ny] == 1:
                    q.append((nx, ny, walls + 1))
        
    return walls
    
def solve():
    m, n = map(int, input().strip().split())
    maze = [list(map(int, input().strip())) for _ in range(n)]
    
    result = bfs(n, m, maze)
    print(result)
if __name__ == "__main__":
    solve()