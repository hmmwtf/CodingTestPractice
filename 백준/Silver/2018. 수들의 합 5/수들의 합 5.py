import sys
input = sys.stdin.readline

N = int(input())
start, end = 1, 1
total = 1
cnt = 0

while start <= N:
    if total < N:
        end += 1
        total += end
    elif total > N:
        total -= start
        start += 1
    else:  
        cnt += 1
        end += 1
        total += end

print(cnt)
