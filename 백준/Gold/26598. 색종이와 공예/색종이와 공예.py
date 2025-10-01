import sys
from collections import deque

input = sys.stdin.readline

def solution():
    n, m = map(int, input().strip().split())
    board = [list(map(str, input().strip())) for _ in range(n)]
    visited = [[False] * m for _ in range(n)]
    directions = [(-1,0), (1,0), (0,-1), (0,1)]
    
    def bfs(si, sj, color):
        q = deque([(si, sj)])
        visited[si][sj] = True
        
        cnt = 0
        min_r = max_r = si
        min_c = max_c = sj
        
        while q:
            i, j = q.popleft()
            cnt += 1
            
            min_r = min(min_r, i)
            max_r = max(max_r, i)
            min_c = min(min_c, j)
            max_c = max(max_c, j)

            for dx, dy in directions:
                nx, ny = i + dx, j + dy
                if 0 <= nx < n and 0 <= ny < m and not visited[nx][ny] and board[nx][ny] == color:
                    q.append((nx, ny))
                    visited[nx][ny] = True
                
        return cnt, min_r, max_r, min_c, max_c
    
    for i in range(n):
        for j in range(m):
            if not visited[i][j]:
                
                color = board[i][j]
                count, min_r, max_r, min_c, max_c = bfs(i, j, color)
                
                square = (max_r - min_r + 1) * (max_c - min_c + 1)
                if count != square:
                    print("BaboBabo")
                    return
    print("dd")
    
if __name__ == "__main__":
    solution()