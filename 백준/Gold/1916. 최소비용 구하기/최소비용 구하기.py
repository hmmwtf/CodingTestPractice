import sys, heapq

input = sys.stdin.readline

n = int(input().strip())
m = int(input().strip())

graph = [{} for _ in range(n + 1)]

for _ in range(m):
    a, b, c = map(int, input().strip().split())
    if b in graph[a]:
        graph[a][b] = min(graph[a][b], c)
    else:
        graph[a][b] = c

def dijkstra(graph, start):
    distances = {node: float('inf') for node in range(1, n+1)}
    distances[start] = 0
    pq = [(0, start)]

    while pq:
        dist, now = heapq.heappop(pq)

        if dist > distances[now]:
            continue

        for adj, w in graph[now].items():
            distance = dist + w

            if distance < distances[adj]:
                distances[adj] = distance
                heapq.heappush(pq, (distance, adj))

    return distances

start, end =map(int, input().strip().split())
distances = dijkstra(graph, start)
print(distances[end])