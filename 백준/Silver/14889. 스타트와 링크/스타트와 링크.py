import sys

input = sys.stdin.readline

def solve():
    n = int(input().strip())
    board = []    
    for i in range(n):
        s = list(map(int, input().strip().split()))
        board.append(s)

    answer = float('inf')
    stack = [(0, [])]
    
    while stack:
        idx, team = stack.pop()
        
        if len(team) == n //2:
            link_team = [x for x in range(n) if x not in team]
            
            score1 = 0
            for i in team:
                for j in team:
                    if i != j:
                        score1 += board[i][j]
            
            score2 = 0
            for i in link_team:
                for j in link_team:
                    if i != j:
                        score2 += board[i][j]
            
            diff = score1 - score2
            if diff < 0:
                diff = (-1) * diff
            answer = min(answer, diff)
            continue
        
        if idx == n:
            continue
        
        stack.append((idx + 1, team + [idx]))
        stack.append((idx + 1, team))
    
    print(answer)
    
if __name__ == "__main__":
    solve()