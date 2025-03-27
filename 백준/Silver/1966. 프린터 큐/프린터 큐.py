import sys
from collections import deque
input = sys.stdin.readline

t = int(input().strip())
result = deque()
for _ in range(t):
    n, m = map(int, input().strip().split())
    x = list(map(int, input().strip().split()))
    
    queue = deque([(i, p) for i, p in enumerate(x)])
    print_count = 0
    
    while queue:
        if any(queue[0][1]  < doc[1] for doc in queue):
            queue.append(queue.popleft())
        else:
            print_count += 1
            idx, _ = queue.popleft()
            if idx == m:
                print(print_count)
                break
        