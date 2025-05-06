import sys
from collections import deque
input = sys.stdin.readline

def solve():
    ans = 1
    
    while sharks:
        i, j = sharks.popleft()
        for di, dj in directions:
            ii, jj = i + di, j + dj
            if 0 <= ii < N and 0 <= jj < M and area[ii][jj] == 0:
                area[ii][jj] = area[i][j] + 1  
                sharks.append((ii, jj))         
                ans = max(ans, area[ii][jj])    

    print(ans - 1)

N, M = map(int, input().split())
area = [list(map(int, input().split())) for _ in range(N)]

directions = [(-1, -1), (-1, 0), (-1, 1), ( 0, -1), ( 0, 1), ( 1, -1), ( 1, 0), ( 1, 1)]  

sharks = deque()
for i in range(N):
    for j in range(M):
        if area[i][j] == 1:
            sharks.append((i, j))

solve()