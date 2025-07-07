import sys

input = sys.stdin.readline

n = int(input().strip())
juan = list(map(int, input().strip().split()))
boss = list(map(int, input().strip().split()))

juan.sort()
boss.sort()

i = 0
j = 0
score = 0

while i < n and j < n:
    if juan[i] < boss[j]:
        score += 1
        i += 1
        j += 1
    else:
        j += 1    
            
if score >= (n+1)//2:
    print("YES")
else:
    print("NO")