import sys
input = sys.stdin.readline

INF = 10**15 

def solution():
    n, m = map(int, input().strip().split())
    
    dist = [[INF] * (n+1) for _ in range(n+1)]
    nxt = [[0] * (n+1) for _ in range(n+1)]
    
    for i in range(1, n+1):
        dist[i][i] = 0
        
    for _ in range(m):
        a, b, w = map(int, input().split())
        if w < dist[a][b]:  
            dist[a][b] = dist[b][a] = w
            nxt[a][b] = b
            nxt[b][a] = a
            

    for k in range(1, n + 1):
        for i in range(1, n + 1):
            dik = dist[i][k]
            if dik == INF:
                continue
            row_i = dist[i]
            row_nxt_i = nxt[i]
            for j in range(1, n + 1):
                alt = dik + dist[k][j]
                if alt < row_i[j]:
                    row_i[j] = alt
                    row_nxt_i[j] = row_nxt_i[k]  
                    
    out_lines = []
    for i in range(1, n + 1):
        row_ans = []
        for j in range(1, n + 1):
            if i == j:
                row_ans.append('-')
            else:
                row_ans.append(str(nxt[i][j]))
        out_lines.append(' '.join(row_ans))
    print('\n'.join(out_lines))

if __name__ == "__main__":
    solution()
