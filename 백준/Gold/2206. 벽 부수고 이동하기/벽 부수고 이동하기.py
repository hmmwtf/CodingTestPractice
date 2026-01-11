import sys
from collections import deque

input = sys.stdin.readline

def bfs(n, m, board):
    direction = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    visitied  = [[[False, False] for _ in range(m)] for _ in range(n)]
    q = deque()
    q.append((0, 0, 0, 1))
    visitied[0][0][0] = True
    
    while q:
        y, x, wall, dist = q.popleft()
        
        if y == n - 1 and x == m - 1:
            return dist
        
        for dx, dy in direction:
            nx = x + dx
            ny = y + dy
            if 0 <= nx < m and 0 <= ny < n:
                if board[ny][nx] == 0 and not visitied[ny][nx][wall]:
                    visitied[ny][nx][wall] = True
                    q.append((ny, nx, wall, dist + 1))
                if board[ny][nx] == 1 and wall == 0 and not visitied[ny][nx][wall]:    
                    visitied[ny][nx][1] = True
                    q.append((ny, nx, 1, dist + 1))
    
    return -1

def solve():
    n, m = map(int, input().strip().split())
    board = [list(map(int, input().strip())) for _ in range(n)]
    result = bfs(n, m, board)
    
    print(result)

if __name__ == "__main__":
    solve()