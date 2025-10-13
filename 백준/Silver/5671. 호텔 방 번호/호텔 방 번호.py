import sys
from collections import Counter

def solution():
    for line in sys.stdin:
        if not line.strip(): 
            continue
        n, m = map(int, line.split())
        print(solve(n, m))

def solve(n, m):
    cnt = 0
    for i in range(n, m + 1):
        s = str(i)
        c = Counter(s)
        flag = True
        for v in c.values():
            if v != 1:
                flag = False
                break
        if flag:
            cnt += 1
    return cnt

if __name__ == "__main__":
    solution()