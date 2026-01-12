import sys
from collections import deque

input = sys.stdin.readline

def bfs(m, n, board):
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    q = deque()
    day = 0
    
    for y in range(n):
        for x in range(m):
            if board[y][x] == 1:
                q.append((x, y, day))
    
    while q:
        x, y, day = q.popleft()
        
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            
            if 0 <= nx < m and 0 <= ny < n and board[ny][nx] == 0:
                board[ny][nx] = 1
                q.append((nx, ny, day + 1))
    
    return day

def solve():
    m, n = map(int, input().strip().split())
    board = [list(map(int, input().strip().split())) for _ in range(n)]
    
    result = bfs(m, n, board)
    
    for y in range(n):
        for x in range(m):
            if board[y][x] == 0:
                result = -1
                break
    
    print(result)

if __name__ == "__main__":
    solve()