import sys
from collections import deque

input = sys.stdin.readline

def solution():
    a, k = map(int, input().strip().split())

    visited = [False] * (k + 1)
    q = deque()
    q.append((a, 0))
    visited[a] = True
    
    while q:
        x, cnt = q.popleft()
        
        if x == k:
            print(cnt)
            return
        
        if x + 1 <= k and not visited[x + 1]:
            visited[x + 1] = True
            q.append((x + 1, cnt + 1))
        
        if 2 * x <= k and not visited[2 * x]:
            visited[2 * x] = True
            q.append((2 * x, cnt + 1))
    
if __name__ == "__main__":
    solution()