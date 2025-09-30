import sys
from collections import deque

input = sys.stdin.readline

def solution():
    n = int(input().strip())
    bridge = list(map(int, input().strip().split()))
    a, b = map(int, input().strip().split())
    
    a -= 1
    b -= 1
    
    visited = [False] * n
    q = deque()
    q.append((a, 0))
    visited[a] = True
    
    while q:
        cur_pos, cur_cnt = q.popleft()
        
        if cur_pos == b:
            print(cur_cnt)
            break
        jump = bridge[cur_pos]
        
        for next_pos in range(cur_pos + jump, n, jump):
            if not visited[next_pos]:
                visited[next_pos] = True
                q.append((next_pos, cur_cnt + 1))

        for next_pos in range(cur_pos - jump, -1, -jump):
            if not visited[next_pos]:
                visited[next_pos] = True
                q.append((next_pos, cur_cnt + 1))
                
    else:
        print(-1)
if __name__ == "__main__":
    solution()