import sys
from collections import deque
input = sys.stdin.readline

def solution():
    n = int(input().strip())
    dq = deque()
    history = []
    
    for i in range(n):
        command = list(map(str, input().strip().split()))
        cmd = command[0]
        
        if cmd == '1':
            ch = command[1]
            dq.append(ch)
            history.append(('R', ch))
        elif cmd == '2':
            ch = command[1]
            dq.appendleft(ch)
            history.append(('L', ch))
        elif cmd == '3':
            if history:
                LR, ch = history.pop()
                if dq:
                    if LR == 'R':
                        value = dq.pop()
                    else:
                        value = dq.popleft()
                else:
                    pass
            else:
                pass
        else:
            print("Invalid Input")
            
    if dq:
        print(''.join(dq))
    else:
        print(0)
    
if __name__ == "__main__":
    solution()