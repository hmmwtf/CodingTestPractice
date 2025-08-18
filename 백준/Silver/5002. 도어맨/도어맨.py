import sys
from collections import deque
input = sys.stdin.readline

x = int(input().strip())
mw = deque(input().strip())

mcnt = wcnt = 0
taken = 0

while mw:
    diff = mcnt - wcnt

    if abs(diff) == x:
        need = 'M' if diff < 0 else 'W'
        if mw[0] == need:
            c = mw.popleft()
            if c == 'M': mcnt += 1
            else: wcnt += 1
            taken += 1
        elif len(mw) >= 2 and mw[1] == need:
            first = mw.popleft()
            second = mw.popleft()  
            if second == 'M': mcnt += 1
            else: wcnt += 1
            mw.appendleft(first)  
            taken += 1
        else:
            break
    else:
        if len(mw) >= 2:
    
            if diff > 0 and mw[0] == 'M' and mw[1] == 'W':
                first = mw.popleft()
                second = mw.popleft()
                wcnt += 1
                mw.appendleft(first)
                taken += 1
                continue
            elif diff < 0 and mw[0] == 'W' and mw[1] == 'M':
                first = mw.popleft()
                second = mw.popleft()
                mcnt += 1
                mw.appendleft(first)
                taken += 1
                continue

        c = mw.popleft()
        if c == 'M': mcnt += 1
        else: wcnt += 1
        taken += 1

print(taken)