import sys
input = sys.stdin.readline

N, M = map(int, input().split())
snow = [1] + list(map(int, input().split()))

def DFS(size, time, idx):
    global result

    if time > M:
        return

    if time <= M:
        result = max(result, size)

    if idx <= N - 1:
        DFS(size + snow[idx+1], time + 1, idx + 1)

    if idx <= N - 2:
        DFS((size // 2) + snow[idx+2], time + 1, idx + 2)

result = 0
DFS(1, 0, 0)
print(result)