import sys
from collections import deque
input = sys.stdin.readline

n = int(input().strip())
q = deque()

for i in range(n):
    q.appendleft(i+1)

while len(q) > 1:
    q.pop()
    num = q.pop()
    q.appendleft(num)

print(q[0])