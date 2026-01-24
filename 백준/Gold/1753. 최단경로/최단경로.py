import sys, heapq

input = sys.stdin.readline

def solve():
    V, E = map(int, input().strip().split())
    K = int(input().strip())
    
    graph = [[] for _ in range(V + 1)]
    dist = [float('inf')] * (V + 1)
    dist[K] = 0
    heap = []
    heapq.heappush(heap, (0, K))
    
    for _ in range(E):
        u, v, w = map(int, input().strip().split())
        graph[u].append((v, w))
        
    while heap:
        d, u = heapq.heappop(heap)
        
        if d > dist[u]:
            continue
        
        for v, w in graph[u]:
            if d + w < dist[v]:
                dist[v] = d + w
                heapq.heappush(heap, ((d + w), v))
    
    for i in range(1, V + 1):
        if dist[i] == float('inf'):
            print("INF")
        else:
            print(dist[i])
    
if __name__ == "__main__":
    solve()