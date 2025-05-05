import sys
sys.setrecursionlimit(10**7)
input = sys.stdin.readline

n, m = map(int, input().split())
graph = [[] for _ in range(n)]

for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

visited = [False] * n
found = False

def dfs(u, depth):
    global found
    if found:
        return
    if depth == 4:
        found = True
        return
    visited[u] = True  
    for v in graph[u]:
        if not visited[v]:
            dfs(v, depth + 1)
    visited[u] = False  

for i in range(n):
    dfs(i, 0)
    if found:
        break

print(1 if found else 0)