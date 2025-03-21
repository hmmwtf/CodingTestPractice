import sys
from collections import deque
input = sys.stdin.readline

def push(queue, val):
    queue.append(val)

def pop(queue):
    if len(queue) == 0:
        return -1
    else:
        return queue.popleft()

def size(queue):
    return len(queue)

def empty(queue):
    if len(queue) == 0:
        return 1
    else:
        return 0

def front(queue):
    if len(queue) == 0:
        return -1
    else:
        return queue[0]
    
def back(queue):
    if len(queue) == 0:
        return -1
    else:
        return queue[-1]

n = int(input().strip())
queue = deque()
for i in range(n):
    order = input().strip().split()
    if order[0] == "push":
        push(queue, order[1])
    elif order[0] == "pop":
        print(pop(queue))
    elif order[0] == "size":
        print(size(queue))
    elif order[0] == "empty":
        print(empty(queue))
    elif order[0] == "front":
        print(front(queue))
    elif order[0] == "back":
        print(back(queue))
    else:
        print("Invalid Input")