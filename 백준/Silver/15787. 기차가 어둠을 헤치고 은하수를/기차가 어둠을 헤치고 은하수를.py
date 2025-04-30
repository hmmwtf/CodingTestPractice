import sys
input = sys.stdin.readline

n, m = map(int, input().split())
trains = [[0]*21 for _ in range(n+1)] 

for _ in range(m):
    cmd, x, *rest = map(int, input().split())
    if cmd == 1:
        y = rest[0]
        trains[x][y] = 1
    elif cmd == 2:
        y = rest[0]
        trains[x][y] = 0
    elif cmd == 3:
        trains[x] = [0, 0] + trains[x][1:20]   
    elif cmd == 4:
        trains[x] = [0] + trains[x][2:21] + [0]

states = set()
for i in range(1, n+1):
    states.add(tuple(trains[i][1:21]))
print(len(states))
