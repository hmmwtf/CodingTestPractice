import sys

input = sys.stdin.readline

n = int(input().strip())
board = [list(map(int, input().split())) for _ in range(n)]

total = 0
maxv = 0
for row in board:
    for x in row:
        total += x
        if x > maxv:
            maxv = x
            
need = (total + 1) // 2

def cnt_cpt(t):
    cnt = 0
    for i in range(n):
        for j in range(n):
            cnt += min(board[i][j], t)
    return cnt

left, right = 0, maxv
answer = maxv

while left <= right:
    mid = (left + right) // 2
    
    if cnt_cpt(mid) >= need:
        answer = mid
        right = mid - 1
    else:
        left = mid + 1
        
print(answer)