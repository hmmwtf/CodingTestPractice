import sys

input = sys.stdin.readline

def solve():
    n, m = map(int, input().strip().split())
    board = [list(map(int, input().strip().split())) for _ in range(n)]
    
    houses, chickens = [], []
    
    for r in range(n):
        for c in range(n):
            if board[r][c] == 1:
                houses.append((r,c))
            elif board[r][c] == 2:
                chickens.append((r,c))

    answer = float('inf')
    stack = [(0, [])]
    
    while stack:
        idx, team = stack.pop()
        
        if len(team) == m:
            total = 0
            
            for hr, hc in houses:
                chicken_dist = float('inf')
                
                for i in team:
                    cr, cc = chickens[i]
                    dist = abs(hr - cr) + abs(hc - cc)
                    chicken_dist = min(chicken_dist, dist)
                
                total += chicken_dist
            
            answer = min(answer, total)
            continue
        
        if idx == len(chickens):
            continue
        
        stack.append((idx + 1, team + [idx]))
        stack.append((idx + 1, team))
        
    print(answer)
    
if __name__ == "__main__":
    solve()