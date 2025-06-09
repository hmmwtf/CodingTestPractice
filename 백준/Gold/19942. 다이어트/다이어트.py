import sys
from itertools import combinations

input = sys.stdin.readline

n = int(input().strip())

mp, mf, ms, mv = map(int, input().strip().split())

min_cost = float('inf')
answer = []

protein, fat, carb, vitamin, cost = [], [], [], [], []

for i in range(n):
    user_input = list(map(int, input().strip().split()))
    protein.append(user_input[0])
    fat.append(user_input[1])
    carb.append(user_input[2])
    vitamin.append(user_input[3])
    cost.append(user_input[4])
    
for r in range(1, n+1):
    for comb in combinations(range(n), r):
        pi = fi = si = vi = ci = 0
        for i in comb:
            pi += protein[i]
            fi += fat[i]
            si += carb[i]
            vi += vitamin[i]
            ci += cost[i]
        
        if pi >= mp and fi >= mf and si >= ms and vi >= mv:
            if ci < min_cost:
                min_cost = ci
                answer = [comb]
            elif ci == min_cost:
                answer.append(comb)

if not answer:
    print(-1)
else:
    answer.sort()
    print(min_cost)
    print(' '.join(str(i+1) for i in answer[0]))