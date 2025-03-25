import sys
from collections import deque
input = sys.stdin.readline

def jp(n, k):
    queue = deque(range(1, n+1))
    result = []
    
    while queue:
        queue.rotate(-(k-1))
        result.append(queue.popleft())
        
    return result

n,k = map(int, input().strip().split())
output = jp(n, k)
print("<" + ", ".join(map(str, output)) + ">")