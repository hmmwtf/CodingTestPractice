import sys

input = sys.stdin.readline

n = input().strip()
l = len(n)

num = int(n)

answer = []

for candi in range(max(1, num - (l * 9)), num + 1):
    nstr = str(candi)
    nsum = 0
    lnstr = len(nstr)
    for i in nstr:
        nsum += int(i)
    
    if candi + nsum == num:
        answer.append(candi)

if len(answer) == 0:
    print(0)
else:
    print(min(answer))