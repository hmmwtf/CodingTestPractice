#boj 25972 도미노 무너뜨리기

import sys
input = sys.stdin.readline

def solution():
    n = int(input().strip())
    
    dominos = []
    for i in range(n):
        ai, li = map(int, input().strip().split())
        dominos.append((ai, li))
        
    dominos.sort()
    ans = 1
    
    max_reach = dominos[0][0] + dominos[0][1]
    
    for i in range(1, n):
        cp = dominos[i][0]
        cl = dominos[i][1]
        
        if cp > max_reach:
            ans += 1
        max_reach = cp + cl
    
    return ans    
    
print(solution())
