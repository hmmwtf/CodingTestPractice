import sys 

input = sys.stdin.readline

n = int(input().strip())

graph = [0] * (n + 1)

for i in range(1, n+1):
    next_senior = int(input().strip())
    graph[i] = next_senior
    
max_cnt = 0
best_start = 1

for i in range(1, n+1):
    visited = [False] * (n + 1)
    cnt = 0
    
    curr = i
    while not visited[curr]:
        visited[curr] = True
        cnt += 1
        curr = graph[curr]
        
    if cnt > max_cnt:
        max_cnt = cnt
        best_start = i

print(best_start)