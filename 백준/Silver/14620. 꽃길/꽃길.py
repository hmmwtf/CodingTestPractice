import sys

input = sys.stdin.readline

n = int(input().strip())
board = [list(map(int, input().strip().split())) for _ in range(n)]
direction = [(-1, 0), (1, 0), (0, -1), (0, 1)]

min_cost = float('inf')
visited = [[False] * n for _ in range(n)]

def isValid(x, y):
    if x < 1 or x >= n-1 or y < 1 or y >= n - 1:
        return False
    
    if visited[x][y]:
        return False
    
    for dx, dy in direction:
        nx = x + dx
        ny = y + dy
        if visited[nx][ny]:
            return False
    return True

def DFS(planted, total, startRow):
    global min_cost, visited
    
    if planted == 3:
        if total < min_cost:
            min_cost = total
        return
    
    for i in range(startRow, n):
        for j in range(n):
            if isValid(i, j):
                cost = board[i][j]
                visited[i][j] = True
                for dx, dy in direction:
                    nx = i + dx
                    ny = j + dy
                    visited[nx][ny] = True
                    cost += board[nx][ny]

                DFS(planted + 1 , total + cost, i)
                
                visited[i][j] = False
                for dx, dy in direction:
                    nx = i + dx
                    ny = j + dy
                    visited[nx][ny] = False

DFS(0, 0, 0)
print(min_cost)