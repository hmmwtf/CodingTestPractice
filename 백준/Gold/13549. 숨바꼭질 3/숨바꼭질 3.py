import sys
from collections import deque

input = sys.stdin.readline

def solve():
    n, k = map(int, input().strip().split())
    result = bfs(n, k)
    print(result)
    
def bfs(n, k):
    visited = [False] * 100001
    q = deque()
    
    visited[n] = True
    q.append((n, 0))
    
    while q:
        x, time = q.popleft()
        
        if x == k:
            break
        
        for nx in [x - 1, x + 1, 2 * x]:
            if 0 <= nx and nx <= 100000 and visited[nx] == False:
                visited[nx] = True
                if nx == 2 * x:
                    q.appendleft((nx, time))
                else:
                    q.append((nx, time + 1))
    return time

if __name__ == "__main__":
    solve()