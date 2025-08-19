import sys

input = sys.stdin.readline

n = int(input().strip())
menus = list(map(int, input().strip().split()))

seen = set()
cur = 0
max_cnt = 0

for x in menus:
    if x not in seen:
        seen.add(x)
        cur += 1
        if cur > max_cnt:
            max_cnt = cur
    else:
        seen.remove(x)
        cur -= 1

print(max_cnt)