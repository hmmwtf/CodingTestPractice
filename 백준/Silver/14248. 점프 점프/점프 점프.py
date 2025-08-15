import sys
from collections import deque

input = sys.stdin.readline

n = int(input().strip())
steps = list(map(int, input().strip().split()))
start = int(input().strip())
visited = [False] * (n + 1)

def BFS(start):
    q = deque()
    visited[start] = True
    q.append(start)
    cnt = 1
    
    while q:
        x = q.popleft()
        for dx in [-steps[x - 1], steps[x - 1]]:
            nx = x + dx
            if 1 <= nx <= n and not visited[nx]:
                visited[nx] = True
                cnt += 1
                q.append(nx)
    
    return cnt

print(BFS(start))