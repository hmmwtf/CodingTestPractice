def dfs(cur):       # 현재 위치(cur) 깊이 우선 방문
    global ans

    v[cur] = 1      # 현재 위치 방문 표시
    ans += 1

    # 연결된 노드/4방향/8방향.. 반복처리
    for nxt in adj[cur]:
        # 범위내, 미방문, 조건에 맞으면 dfs 호출
        if v[nxt] == 0:
            dfs(nxt)

N = int(input())
M = int(input())
adj =[[] for _ in range(N+1)]
for _ in range(M):
    s,e = map(int, input().split())
    adj[s].append(e)
    adj[e].append(s)    #양방향

ans = 0
v = [0]*(N+1)
dfs(1)                  # 1번 컴퓨터가 감염시킴

print(ans -1)