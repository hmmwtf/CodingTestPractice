# boj 15723(n단 논법)
import sys
input = sys.stdin.readline

def dfs(start, target, visited, graph):
    if start == target:
        return True
    
    visited.add(start)
    
    if start in graph:
        for next in graph[start]:
            if next not in visited:
                if dfs(next, target, visited, graph):
                    return True
    
    return False

def solution():
    n = int(input().strip())
    graph = {}
    for i in range(n):
        sen = input().strip().split(' is ')
        start = sen[0]
        end = sen[1]
        if start not in graph:
            graph[start] = []
        graph[start].append(end)
        
    m = int(input().strip())
    out = []
    for i in range(m):
        result_sen = input().strip().split(' is ')
        s = result_sen[0]
        t = result_sen[1]
        out.append('T' if dfs(s, t, set(), graph) else 'F')

    return '\n'.join(out)

print(solution())
